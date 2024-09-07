$(document).ready(function (){

    $(function () {
        $("#upload-area").hover(function () {
        $(this).css({'border':'1px dashed #1E9FFF'});
    },function () {
            $(this).css({'border':'0px dashed #1E9FFF'});
        })
    });

$("#upload-candidate").click(function () {

   $("#file-upload").click();
});



$(".btn.btn-primary.add").click(function () {

     var educationpane =  $(this).parent().parent().children(":first")[0].cloneNode(true);

    educationpane.style.display = "block";

    $(this).parent().before(educationpane);

});
$(".btn.btn-secondary.del").click(function () {

    var educationpane = $(this).parent().parent().children(":first")[0];


    if($("." + educationpane.className).length > 1){

        var name = "." + educationpane.className + ":last";

        $(name).remove();
    }

});





    function fillFrom(name,data) {
        data = data.replace(/&amp;/g, "&");
        data = data.split('|');
        var add = $(`.${name}`).parent().children(":last").children(":first");
        var del = $(`.${name}`).parent().children(":last").children(":last");
        $.each(data,function (index,value){
            if(value==='') return false;
        $.each(JSON.parse(formToJson(value)),function (key,value) {
            $(`.${name}`).eq(index + 1).find(`input[name=${key}]`).val(decodeURIComponent(value));
            if(key==="project_describe"){
                $(`.${name}`).eq(index + 1).find(`textarea[name=${key}]`).val(decodeURIComponent(value));
            }
        });
        add.click();
    });
    del.click()
    }

     fillFrom("social",social);
    fillFrom("award",award);
    fillFrom("education",education);
    fillFrom("project",project);

    $.each(JSON.parse(formToJson(advantage)),function (key,value) {
       $('textarea[name=' + key + ']').val(decodeURIComponent(value));
    });

    $.each(JSON.parse(formToJson(evaluation)),function (key,value) {
       $('textarea[name=' + key + ']').val(decodeURIComponent(value));
    });


});

function formToJson(data){
    data = data.replace(/&/g,"\",\"");
    data = data.replace(/=/g,"\":\"");
    data = "{\"" + data + "\"}";


    return data;

}
function formToJsonSever(data){
    data = decodeURIComponent(data);
    data = data.replace(/&/g,"\",\"");
    data = data.replace(/=/g,"\":\"");
    data = "{\"" + data + "\"}";


    return data;

}

$(document).ready(function() {

    $.validator.setDefaults({
       errorPlacement: function(error, element) {
        var name = element.attr('name');
        var pclassName = element.parent().parent()[0].className;


           if(name.endsWith("time")){
               $(`.${pclassName} label[for=${name}]`).html(error);
           }
           else{
                error.insertAfter(element);
           }
    }

    });

    $("#candidate-form").validate({


    rules: {
        name : {
            required: true,
            minlength: 3,
        },
        phone: {
            required:true,
            mobile:true,

        },
        email: {
            required: true,
        },

        intention:{
          required:true,
        },
        self_advantage:{
            required:true,
        },
        school: {
              required: true,

        },
        education_background: {
            required:true,
        },
        major:{
            required:true,
        },
        start_time:{
            required:true,
        },
        end_time:{
            required:true,
        },
        grade_rank:{
          required:true,
        },
        project_name:{
            required:true,
        },
        project_role:{
            required:true,
        },
        project_starttime:{
            required:true,
        },
        project_endtime:{
            required:true,
        },
        project_link:{
            required:true,
        },
        project_describe:{
            required:true,
        },
        self_evaluation:{
            required:true,
        }


    },
    messages: {
        name : {
            required: "姓名不能为空",
            minlength: "名字长度不能小于3",
        },
        phone: {
            required:"手机号不能为空",
            mobile:"请正确填写手机号",

        },
        email: {
            required: "邮箱不能为空",
        },

        intention:{
          required:"求职意向不能为空",
        },
        self_advantage:{
            required:"个人优势不能为空",
        },
        school: {
              required: "学校不能为空",

        },
        education_background: {
            required:"学历不能为空",
        },
        major:{
            required:"专业不能为空",
        },
        start_time:{
            required:"开始时间不能为空",
        },
        end_time:{
            required:"结束时间不能为空",
        },
        grade_rank:{
          required:"成绩排名不能为空",
        },
        project_name:{
            required:"项目名称不能为空",
        },
        project_role:{
            required:"项目角色不能为空",
        },
        project_starttime:{
            required:"项目开始时间不能为空",
        },
        project_endtime:{
            required:"项目结束时间不能为空",
        },
        project_link:{
            required:"项目链接不能为空",
        },
        project_describe:{
            required:"项目描述不能为空",
        },
        self_evaluation:{
            required:"个人评价不能为空",
        },

    },
    submitHandler: function (form) {
        ajaxSubmit();
    }



});

$.validator.addMethod("mobile", function(value, element) {
            var length = value.length;
            return this.optional(element) || (length == 11 && /^1[3456789]\d{9}$/.test(value));
        }, function () {
        return "手机号码格式错误!";
});



});


 function ajaxSubmit() {
        // 阻止表单默认提交行为

        var jsonData = {};

        jsonData["social"] = "";
        jsonData["project"] = "";
        jsonData["education"] = "";
        jsonData["award"] = "";

        $(".baseinfo").each(function () {


            var seriData = $(this).find('input').serialize();

            var data = formToJsonSever(seriData);

            jsonData["baseinfo"] = data;

        });


        $(".social:gt(0)").each(function () {
            var seriData = $(this).find('input').serialize() + "|";
            jsonData["social"] += seriData;

        });

        $(".award:gt(0)").each(function () {


            var seriData = $(this).find('input').serialize() + "|";


            jsonData["award"] += seriData;
        });

        $(".education:gt(0)").each(function () {

            var seriData = $(this).find('input').serialize() + "|";


            jsonData["education"] += seriData;
        });


        $(".project:gt(0)").each(function () {


            var seriData = $(this).find('input').serialize();
            var describe = $(this).find('textarea').serialize();
            seriData = seriData + "&" + describe + "|";

            jsonData["project"] += seriData;
        });

        var data = $(".self").find('textarea').serialize();

        jsonData["self"] = data;

        var data = $(".advantage").find('textarea').serialize();


        jsonData["advantage"] = data;


        $.ajax({
            url: 'http://192.168.160.114:8000/editcandidate/',
            type: 'post',
            headers: {"X-CSRFToken": $.cookie('csrftoken')},
            data: jsonData,
            success: function (data1) {

                window.location.href='/mycandidate/';

            }
        });
    }
