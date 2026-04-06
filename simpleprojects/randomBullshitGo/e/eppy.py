poem = "Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are"

# Split the poem into lines
lines = poem.split("\n")

# Add indentation manually
formatted_poem = f"""{lines[0]}
    {lines[1]}
        {lines[2]}
        {lines[3]}
{lines[4]}
    {lines[5]}"""

print(formatted_poem)
