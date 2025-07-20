document.addEventListener('DOMContentLoaded', () => {
  const toggleHeader = document.querySelector('#toggle_header');
  const header = document.querySelector('header');

  toggleHeader.addEventListener('click', () => {
    if (header.classList.contains('red')) {
      header.classList.replace('red', 'green');
    } else if (header.classList.contains('green')) {
      header.classList.replace('green', 'red');
    }
  });
});
