$(document).ready(function(){
    $('.loadcontent').click(function(){
        var video = $(this).children('span');
        var src = video.html();
        $('body,html').animate({scrollTop:0},1000);
        $.post('/getvideo/',{'src':src},function(data){
            $('.video-top-outer').empty().append(data);
        });
        //var top_video = $('.video-top');
        //top_video.attr('src',src);
        return false;
    })
});

