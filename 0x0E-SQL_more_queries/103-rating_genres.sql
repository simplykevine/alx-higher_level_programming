-- Prints and joins records from two tables with a matching field
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
    FROM tv_genres
    LEFT JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
    RIGHT JOIN tv_show_ratings
        ON tv_show_ratings.show_id = tv_show_genres.show_id
    WHERE tv_genres.name IS NOT NULL
    GROUP BY tv_genres.id
    ORDER BY rating DESC;
