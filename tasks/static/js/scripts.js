// tasks/static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    const taskList = document.querySelector('ul');

    taskList.addEventListener('click', function(event) {
        if (event.target.tagName === 'LI') {
            event.target.classList.toggle('done');
        }
    });
});
