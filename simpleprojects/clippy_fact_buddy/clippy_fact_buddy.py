#!/usr/bin/env python3
import sqlite3
import tkinter as tk
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "facts.db"


def connect_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


class FactDatabase:
    def __init__(self, path: Path):
        self.path = path
        self.conn = connect_db()
        self._create_tables()

    def _create_tables(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS facts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fact_text TEXT NOT NULL UNIQUE
            )
            """
        )
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
            """
        )
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS fact_tags (
                fact_id INTEGER NOT NULL,
                tag_id INTEGER NOT NULL,
                PRIMARY KEY (fact_id, tag_id),
                FOREIGN KEY (fact_id) REFERENCES facts(id) ON DELETE CASCADE,
                FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
            )
            """
        )
        self.conn.commit()

    def add_fact(self, fact_text: str, tags: list[str]):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM facts WHERE fact_text = ?", (fact_text,))
        row = cursor.fetchone()
        if row:
            fact_id = row[0]
        else:
            cursor.execute("INSERT INTO facts (fact_text) VALUES (?)", (fact_text,))
            fact_id = cursor.lastrowid

        for tag in tags:
            tag_name = tag.strip().lower()
            if not tag_name:
                continue
            cursor.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (tag_name,))
            cursor.execute("SELECT id FROM tags WHERE name = ?", (tag_name,))
            tag_id = cursor.fetchone()[0]
            cursor.execute(
                "INSERT OR IGNORE INTO fact_tags (fact_id, tag_id) VALUES (?, ?)",
                (fact_id, tag_id),
            )
        self.conn.commit()

    def find_random_fact(self, tag: str) -> str | None:
        search_tag = tag.strip().lower()
        if not search_tag:
            return None

        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT f.fact_text
            FROM facts f
            JOIN fact_tags ft ON f.id = ft.fact_id
            JOIN tags t ON t.id = ft.tag_id
            WHERE t.name = ?
            ORDER BY RANDOM()
            LIMIT 1
            """,
            (search_tag,),
        )
        row = cursor.fetchone()
        if row:
            return row[0]

        cursor.execute(
            """
            SELECT f.fact_text
            FROM facts f
            JOIN fact_tags ft ON f.id = ft.fact_id
            JOIN tags t ON t.id = ft.tag_id
            WHERE t.name LIKE ?
            ORDER BY RANDOM()
            LIMIT 1
            """,
            (f"%{search_tag}%",),
        )
        row = cursor.fetchone()
        return row[0] if row else None


class ClippyFactBuddyApp:
    def __init__(self, db: FactDatabase):
        self.db = db
        self.root = tk.Tk()
        self.root.title("Clippy Fact Buddy")
        self.root.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        frame = tk.Frame(self.root, padx=12, pady=12)
        frame.pack()

        icon = self._load_icon()
        if icon:
            icon_button = tk.Button(
                frame,
                image=icon,
                command=self._open_query_dialog,
                borderwidth=0,
                highlightthickness=0,
                activebackground=self.root.cget("bg"),
            )
            icon_button.image = icon
            icon_button.pack()
        else:
            icon_button = tk.Button(
                frame,
                text="Clippy Fact Buddy",
                command=self._open_query_dialog,
                width=18,
                height=4,
            )
            icon_button.pack()

        info = tk.Label(
            frame,
            text="Click the icon to enter a tag and get a single fact.",
            wraplength=220,
            justify="center",
            pady=8,
        )
        info.pack()

    def _load_icon(self) -> tk.PhotoImage | None:
        icon_path = Path(__file__).resolve().parent / "clippy_icon.png"
        if icon_path.exists():
            try:
                return tk.PhotoImage(file=str(icon_path))
            except tk.TclError:
                return None
        return None

    def _open_query_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Ask for a fact")
        dialog.resizable(False, False)
        dialog.grab_set()

        tk.Label(dialog, text="Tag:").grid(row=0, column=0, sticky="w", padx=8, pady=(12, 4))
        tag_entry = tk.Entry(dialog, width=32)
        tag_entry.grid(row=0, column=1, padx=8, pady=(12, 4))
        tag_entry.focus()

        result_label = tk.Label(dialog, text="", wraplength=320, justify="left")
        result_label.grid(row=2, column=0, columnspan=2, padx=8, pady=(8, 12))

        def on_search():
            tag = tag_entry.get().strip()
            if not tag:
                result_label.config(text="Please enter a tag like furry, warframe, or atoms.")
                return
            fact = self.db.find_random_fact(tag)
            if fact:
                result_label.config(text=fact)
            else:
                result_label.config(
                    text=(
                        "No fact found for that tag yet. "
                        "Try another tag or add more facts to the database."
                    )
                )

        search_button = tk.Button(dialog, text="Get Fact", command=on_search)
        search_button.grid(row=1, column=0, columnspan=2, pady=(4, 0))

        dialog.bind("<Return>", lambda event: on_search())

    def run(self):
        self.root.mainloop()


def main():
    db = FactDatabase(DB_PATH)
    app = ClippyFactBuddyApp(db)
    app.run()


if __name__ == "__main__":
    main()
