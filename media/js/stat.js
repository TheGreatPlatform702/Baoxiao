$('.datetimepicker').datetimepicker({
    format: 'yyyy-mm-dd'
});

$("#search-submit-btn").click(function(){
    var form = $("#search-form").serialize(true);
    Dajaxice.statistic.search(search_callback, {"form": form});
});

function search_callback(data){
    if(data['statu'] == 0) {
        $('.result-table').html(data['html']);
    } else {
        alert('Something wrong');
    }
}