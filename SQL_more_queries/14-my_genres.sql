-- Lists the genres of 'Dexter'
SELECT tv_genres.name AS name
FROM tv_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id = ( SELECT tv_shows.id FROM tv_shows WHERE tv_shows.title = 'Dexter' )
ORDER BY tv_genres.name ASC; 
