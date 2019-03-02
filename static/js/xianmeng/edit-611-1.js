$(document).ready(function () {




    sessionStorage.setItem('staticNum', $(".compNumber")[0].value);
    $(".compNumber111111111").on('input propertychange', function (e) {   //实时获取所属产业单位数
        // console.log($('.comp_611_1').length)
        var staticNum = sessionStorage.getItem('staticNum');
        $(".new-parent-row").html("");   //清空机构
        var changeNum = 0;
        if ($('.comp_611_1').length < this.value) {
            // console.log($('.comp_611_1').length)
            changeNum = this.value - $('.comp_611_1').length
            for (let i = 0; i < changeNum; i++) {
                // $("#comp-card").append(
                e.preventDefault()
                // form id like #id_form-TOTAL_FORMS
                var formId = "id_form-TOTAL_FORMS"
                // copy empty form
                var emptyRow = $("#empty-row").clone();
                // remove id from new form
                emptyRow.attr("id", null)
                emptyRow.attr('class', 'comp_611_1');
                emptyRow.attr('class', 'white-box');
                // Insert row after last row
                // get starting form count for formset
                var totalForms = parseInt($('#' + formId).val());
                // create new form row from empty form row
                var newFormRow;
                emptyRow.find("input, select, textarea").each(function () {
                    newFormRow = updateEmptyFormIDs($(this), totalForms)
                })
                // insert new form at the end of the last form row
                $(".comp_611_1:last").after(newFormRow)

                // update total form count (to include new row)
                $('#' + formId).val(totalForms + 1);

                // scroll page to new row
                $('html, body').animate({
                    scrollTop: newFormRow.offset().top - 100
                }, 500, function () {
                    // animate background color
                    // requires: jQuery Color: https://code.jquery.com/color/jquery.color-2.1.2.min.js
                    newFormRow.animate({
                        backgroundColor: "#fff"
                    }, 1500)
                });

            }
        }
        console.log(this.value)
        console.log(staticNum)
        console.log($('.comp_611_1').length)
        if ((this.value >= staticNum) && ($('.comp_611_1').length > this.value)) {
            changeNum = $('.comp_611_1').length - this.value;
            for (let i = 1; i <= changeNum; i++) {
                $('.comp_611_1:eq(-1)').remove()
            }
        }
    });


    // $('.deleteBtn').click(function (e) {
    //     e.preventDefault()
    //     console.log(e)
    // })

})