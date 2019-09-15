$(document).ready(function(){
    $(window).scroll(function(){
        var top = $(window).scrollTop();
        if(top < 100){
            $("#toTop").hide();
        }else{
            $("#toTop").show();
        }
    });

    $("#toTop").click(function(){
        $(window).scrollTop(0);
    });

    
});