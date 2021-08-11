square = []
for i in range(1,11):
    square.append(i**2)
print(square)


new_sqr = [i**2 for i in range(1,11)]
print(new_sqr)


movie = [("death", 2012), ("gameoflove", 2011), ("myWorld", 2008), ("lordIf", 2001), ("jackSparrow", 2015)]

movie_list = [title for title, year in movie if year>2010]
print(movie_list)