function air_in(){
    let box =  $('#in-con');
    if(box.is(':visible') === true){
            box.hide();
    }else{
            box.show();
    }
}

function air_out(){
    let box =  $('#out-con');
    if(box.is(':visible') === true){
            box.hide();
    }else{
            box.show();
    }
}

$(function() {
    $( "#togoDatepicker" ).datepicker({
         changeMonth: true, 
         dayNames: ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일'],
         dayNamesMin: ['월', '화', '수', '목', '금', '토', '일'], 
         monthNamesShort: ['1','2','3','4','5','6','7','8','9','10','11','12'],
         monthNames: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']
    });

    $( "#comeDatepicker" ).datepicker({
        changeMonth: true, 
        dayNames: ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일'],
        dayNamesMin: ['월', '화', '수', '목', '금', '토', '일'], 
        monthNamesShort: ['1','2','3','4','5','6','7','8','9','10','11','12'],
        monthNames: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']
   });
});