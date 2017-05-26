$(document).ready(function(){
    $("#login-btn").click(function(){
        form = $("#loginform").serialize(true);
        Dajaxice.registration.login(login_callback, {'form': form});
    });
})

function login_callback(data){
    if(data["statu"] == 1) alert("信息有误");
    else {
        location.reload();
    }
}