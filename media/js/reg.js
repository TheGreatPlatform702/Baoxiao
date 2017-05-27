$(document).ready(function(){
    $("#reg-btn").click(function(){
        password = $('#id_password').val()
        confirm_password = $('#id_confirm_password').val()
        if(password == confirm_password) {
            form = $("#reg-form").serialize(true);
            Dajaxice.registration.register(register_callback, {'form': form});
        } else {
            alert("密码输入不一致");
        }
    });
})

function register_callback(data){
    if(data["statu"] == 1) alert("注册失败，学号已存在");
    else {
        location.reload();
    }
}