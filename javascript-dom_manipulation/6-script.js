document.addEventListener('DOMContentLoaded', () => {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      const characterDiv = document.querySelector('#character');
      characterDiv.textContent = data.name;
    })
    .catch(error => console.error('Fetch error:', error));
});
