$(document).ready(function(){
    $('.photo').hover(
        function(){
        $(this).children('.quan').fadeIn()
    },
        function(){
        $(this).children('.quan').fadeOut()
        }
    )
});
