(function ($) {

    // fetching list template
    $("#fetch-list-temp").click(fetchList);

    // fetching template for creation
    $("#fetch-temp").click(fetchTemp);

    // fetching templates for edition or deletion
    $("#list-wrapper").on("click", "#fetch-temp", fetchTemp);

    // submiting template for creation, edition or deletion 
    $(".modal").on("submit", "#submit-temp", submitTemp);


    /////////////////////// handler functions /////////////////////// 

    // fetch list template and put it in our page
    function fetchList() {
        var btn = $(this);
        $.ajax({
            url: btn.attr('data-url'), 
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                console.log('fetching list template from server ... ')
            },
            success: function (data) {
                $("#list-wrapper").html(data.list_temp); // set template in our page
            }
        });
    }

    // fetch create, edit or delete template and put it in our page
    function fetchTemp() {
        var btn = $(this);
        $.ajax({
            url: btn.attr('data-url'),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $(".modal").modal("show"); 
            },
            success: function (data) {
                $(".modal-content").html(data.temp); // set template in our page
            }
        });
    }

    // submit create, edit or delete templates and get back list template
    function submitTemp() {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data) {
                if (data.form_is_valid) { // set list template in our page
                    $(".modal").modal("hide"); 
                    $("#list-wrapper").html(data.list_temp); 
                }
                else { // set template in our page with errors
                    $(".modal-content").html(data.temp); 
                }
            }
        });
        return false;
    }

})(jQuery);
