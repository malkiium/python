ABILITY_STRENGTH_MODS = [
    {"name": "Blind Rage", "strength": 99, "slots": 1},
    {"name": "Transient Fortitude", "strength": 55, "slots": 1},
    {"name": "Intensify", "strength": 30, "slots": 1},
    {"name": "Umbral Intensify", "strength": 44, "slots": 1},
    {"name": "Power Drift", "strength": 15, "slots": 1},
    {"name": "Augur Secrets", "strength": 24, "slots": 1},
]

SPRINT_SPEED_MODS = [
    {"name": "Rush", "sprint": 30, "slots": 1},
    {"name": "Amar's Anguish", "sprint": 15, "parkour": 15, "slots": 1},
    {"name": "Armored Agility", "sprint": 15, "slots": 1},
    {"name": "Speed Drift", "sprint": 12, "slots": 1},
]

ALL_MODS = ABILITY_STRENGTH_MODS + SPRINT_SPEED_MODS

CONFLICTS = [
    ("Intensify", "Umbral Intensify"),
]

def generate_combinations(mods, r):
    """Generate all combinations of r mods from the list"""
    n = len(mods)
    if r > n:
        return
    
    indices = list(range(r))
    yield [mods[i] for i in indices]
    
    while True:
        i = r - 1
        while i >= 0 and indices[i] == i + n - r:
            i -= 1
        
        if i < 0:
            return
        
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        
        yield [mods[i] for i in indices]

def has_conflicts(mod_combo):
    """Check if a mod combination has conflicting mods"""
    mod_names = [mod["name"] for mod in mod_combo]
    
    for conflict_pair in CONFLICTS:
        if conflict_pair[0] in mod_names and conflict_pair[1] in mod_names:
            return True
    return False

def calculate_stats(mod_combo):
    """Calculate total AS and SS from a mod combination"""
    total_strength = 130
    total_sprint = 100
    total_slots = 0
    
    for mod in mod_combo:
        total_strength += mod.get("strength", 0)
        total_sprint += mod.get("sprint", 0)
        total_slots += mod["slots"]
    
    return total_strength, total_sprint, total_slots

def M(as_percent, ss_percent):
    """Volt Speed formula: SS * (1 + (AS/100 * 0.75))"""
    return ss_percent * (1 + (as_percent / 100 * 0.75))

def find_best_build(max_slots=9):
    best_speed = 0
    best_combo = None
    best_stats = None
    
    print(f"Testing all combinations with <={max_slots} mod slots...")
    print("-" * 80)
    
    total_combos = 0
    valid_combos = 0
    
    for r in range(1, len(ALL_MODS) + 1):
        for combo in generate_combinations(ALL_MODS, r):
            total_combos += 1
            
            if has_conflicts(combo):
                continue
                
            strength, sprint, slots = calculate_stats(combo)
            
            if slots <= max_slots:
                valid_combos += 1
                speed = M(strength, sprint)
                
                if speed > best_speed:
                    best_speed = speed
                    best_combo = combo
                    best_stats = (strength, sprint, slots)
    
    print(f"Tested {total_combos} combinations ({valid_combos} valid)\n")
    
    if best_combo:
        strength, sprint, slots = best_stats # type: ignore
        print(f"BEST BUILD FOUND:")
        print(f"Effective Speed: {best_speed:.2f}")
        print(f"Ability Strength: {strength}%")
        print(f"Sprint Speed: {sprint}%")
        print(f"Slots Used: {slots}/{max_slots}")
        print(f"\nMods ({len(best_combo)}):")
        
        str_mods = [m for m in best_combo if "strength" in m]
        sprint_mods = [m for m in best_combo if "sprint" in m]
        
        if str_mods:
            print("\n  Ability Strength:")
            for mod in str_mods:
                print(f"    - {mod['name']}: +{mod['strength']}%")
        
        if sprint_mods:
            print("\n  Sprint Speed:")
            for mod in sprint_mods:
                print(f"    - {mod['name']}: +{mod['sprint']}%")
    
    return best_combo, best_stats, best_speed

find_best_build(max_slots=9)