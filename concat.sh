#!/bin/zsh

# Output file
output_file="src/code.txt"

# Nettoyage de la sortie si elle existe
rm -f "$output_file"

# Add generated date and time at the top
echo "Generated $(date '+%Y-%m-%d %H:%M:%S')" >> "$output_file"
echo "\n\n" >> "$output_file"

# Find all .py files recursively inside src, sort alphabetically, handle spaces
find src -type f -name "*.py" | sort | while IFS= read -r f; do
    echo "===========================================================================================" >> "$output_file"
    echo "    $f " >> "$output_file"
    echo "===========================================================================================" >> "$output_file"
    cat "$f" >> "$output_file"
    echo "\n\n" >> "$output_file"
done

echo "Concaténation terminée → $output_file généré"
