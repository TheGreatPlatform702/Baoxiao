$(document).ready(function(){
    $("#baoxiao-submit-btn").click(function(){
        forms = $(".baoxiao-form");
        var serialized_forms = new Array()
        for(var i = 0; i < forms.length; i++) {
            var tmp_form = $(forms[i]).serialize(true);
            serialized_forms.push(tmp_form);
        }
        Dajaxice.bills.baoxiao(submit_Baoxiao_callback, {"forms": serialized_forms});
    });
})

function submit_Baoxiao_callback(data){
    if(data['statu'] == -1) alert("提交成功");
    else alert("Something Wrong");
}
