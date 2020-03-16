/*
function purchase_toggle() {
    let chk_pur = $('#purchase_box');
    if(chk_pur.is(':visible') === true){
        chk_pur.hide();
        $('#purchase').text('구매하기');
    }else{
        chk_pur.show();
        $('#purchase').text('주문취소');
    }
}

function success() {
    let chk_tt = $('#phone-number, #validationTextarea').val();
    if(chk_tt === ''){
        alert('입력을 완료하세요!');
    }else{
        alert('주문 성공!');
    }
}

function selPayment() {
    $('#pay1').click(function () {
        $('#sel-card').addClass('active');
        $('#sel-cash, #sel-kakao').removeClass('active');
    });

    $('#pay2').click(function () {
        $('#sel-cash').addClass('active');
        $('#sel-card, #sel-kakao').removeClass('active');
    });

    $('#pay3').click(function () {
        $('#sel-kakao').addClass('active');
        $('#sel-card, #sel-cash').removeClass('active');
    });
}
*/

const purchase_toggle = () => {
    let chk_pur = $('#purchase_box');
    if(chk_pur.is(':visible') === true){
        chk_pur.hide();
        $('#purchase').text('구매하기');
    }else{
        chk_pur.show();
        $('#purchase').text('주문취소');
    }
};

const success = () => {
    let chk_tt = $('#phone-number, #validationTextarea').val();
    if(chk_tt === ''){
        alert('입력을 완료하세요!');
    }else{
        alert('주문 성공!');
    }
};

const selPayment = () => {
    $('#pay1').click(function () {
        $('#sel-card').addClass('active');
        $('#sel-cash, #sel-kakao').removeClass('active');
    });

    $('#pay2').click(function () {
        $('#sel-cash').addClass('active');
        $('#sel-card, #sel-kakao').removeClass('active');
    });

    $('#pay3').click(function () {
        $('#sel-kakao').addClass('active');
        $('#sel-card, #sel-cash').removeClass('active');
    });
};

selPayment();