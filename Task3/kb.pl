:- dynamic book/1.
:- dynamic genre/2.

book('The Great Gatsby').
book('1984').
book('Brave New World').
book('The Song of Achilles').
book('The Picture of Dorian Gray').
book('War and Peace').

genre('The Great Gatsby', 'Classic').
genre('1984', 'Dystopian').
genre('Brave New World', 'Dystopian').
genre('The Song of Achilles', 'Greek Retelling').
genre('The Picture of Dorian Gray', 'Classic').
genre('War and Peace', 'Historical Fiction').


recommend_book(Book1,Book2) :- 
    genre(Book1, Genre),
    genre(Book2, Genre),
    Book1 \= Book2.
