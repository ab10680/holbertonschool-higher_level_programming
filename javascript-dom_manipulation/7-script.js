document.addEventListener('DOMContentLoaded', () => {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const moviesList = document.querySelector('#list_movies');
      data.results.forEach(film => {
        const li = document.createElement('li');
        li.textContent = film.title;
        moviesList.appendChild(li);
      });
    })
    .catch(error => console.error('Fetch error:', error));
});
