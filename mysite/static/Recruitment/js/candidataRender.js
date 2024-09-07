$(document).ready(function () {

    function datafill(name,data){
        data = data.replace(/&amp;/g,"&");
        data = data.split("|");

    $.each(data,function (index,value) {

        if(value==="") return false;

        var content  = $(`#${name}-content`).children(":first")[0].cloneNode(true);
        content.style.display = "flex";

        $(`.${name}.row:last`).after(content);

        $.each(JSON.parse(formToJson(value)),function (key,value) {
            $(`.${name}.row`).eq(index + 1).find(`span[data-name=${key}]`).html(decodeURIComponent(value));

        });

    })

    }


    datafill("education",education);
    datafill("award",award);
    datafill("project",project);
    datafill('social',social);
    datafill('advantage',advantage);
    datafill('evaluation',evaluation);



    function formToJson(data){
    data = data.replace(/&/g,"\",\"");
    data = data.replace(/=/g,"\":\"");
    data = "{\"" + data + "\"}";


    return data;

}



});