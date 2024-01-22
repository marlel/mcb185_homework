gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -E ".{4,}" | grep -v -E "[^zonicar]"
# Co-authored with Jon Raigosa
