$(document).ready(function(){
    $("#reg-btn").click(function(){
        alert("hll");
        form = $("#reg-form").serialize(true);
        Dajaxice.registration.register(register_callback, {'form': form});
    });
})

function register_callback(data){
    if(data["statu"] == 1) alert("注册失败");
    else {
        location.reload();
    }
}