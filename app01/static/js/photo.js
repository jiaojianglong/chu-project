$(document).ready(function(){
    $('[type=file]').change(function(e) {
        var file = e.target.files[0];
        var img = new Image(), url = img.src = URL.createObjectURL(file);
        var $img = $(img);
        img.onload = function () {
            URL.revokeObjectURL(url);
            $('#preview').empty().append($img)
        }
    });
    $('.load-exit').click(function(){
       $('#load').fadeOut()
    });
    $('.upload-photo').click(function(){
        $('#load').fadeIn();
    });
    $('.login-exit').click(function(){
       $('#login').fadeOut()
    });
    $('.keai_login').click(function(){
       $('#login').fadeIn()
    });

});
