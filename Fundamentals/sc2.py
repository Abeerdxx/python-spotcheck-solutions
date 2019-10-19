favorite_genre = "Fantasy"
has_spare_time = False
is_employed = False

print("Should you watch Lord of the Rings?")
print( (has_spare_time and (favorite_genre == "Fantasy")) or (not is_employed) )

# Output: True
# Break down:

(has_spare_time and (favorite_genre == "Fantasy")) or (not is_employed)
#                   |------------True-----------|

(has_spare_time and True) or (not is_employed)
#|----False---|

(False and True) or (not is_employed)
#                       |---False---|

(False and True) or (not False)
#|----False----|


(False or (not False))
#         |---True---|

(False or True)
(True)
