document.addEventListener('DOMContentLoaded', function() {
    const taskItems = document.querySelectorAll('li');

    taskItems.forEach(item => {
        item.addEventListener('click', function() {
            item.classList.toggle('done');
        });
    });
});
