var editor = document.querySelector('#editor')
var editor_numeration = document.querySelector('#editor_numeration')

editor.addEventListener('scroll', function() {
    editor_numeration.scrollTop = editor.scrollTop;
    editor_numeration.scrollLeft = editor.scrollLeft;
});

editor_numeration.addEventListener('scroll', function() {
    editor.scrollTop = editor_numeration.scrollTop;
    editor.scrollLeft = editor_numeration.scrollLeft;
});