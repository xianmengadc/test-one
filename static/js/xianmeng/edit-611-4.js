$(document).ready(function () {



    $(".compNumber").on('input propertychange', function (e) {   //实时获取所属产业单位数
        console.log(this.value)
        $(".new-parent-row").html("");   //清空机构
        for (let i = 1; i <= this.value; i++) {
            // $("#comp-card").append(
                e.preventDefault()
            // form id like #id_form-TOTAL_FORMS
            var formId = "id_form-TOTAL_FORMS"

            // copy empty form
            var emptyRow = $("#empty-row").clone();
            // remove id from new form
            emptyRow.attr("id", null)
            // Insert row after last row

            // get starting form count for formset
            var totalForms = parseInt($('#' + formId).val());
            // create new form row from empty form row
            var newFormRow;
            emptyRow.find("input, select, textarea").each(function(){
                newFormRow = updateEmptyFormIDs($(this), totalForms)
            })


            // insert new form at the end of the last form row
            $(".comp_611_4:last").after(newFormRow)

            // update total form count (to include new row)
            $('#'+ formId).val(totalForms + 1);

            // scroll page to new row
            $('html, body').animate({
                scrollTop: newFormRow.offset().top - 100
            }, 500, function(){
                // animate background color
                // requires: jQuery Color: https://code.jquery.com/color/jquery.color-2.1.2.min.js
                newFormRow.animate({
                    backgroundColor: "#fff"
                }, 1500)
            });


                // `
                // <div>
                //     <div class="col-md-6">
                //     <p>机构 ${i}</p>
                //             <div class="form-group">
                //                 <label for="unit_category" class="col-sm-6 control-label">单位类别</label>
                //                 <div class="col-sm-6">
                //                     <input type=" text" class="form-control" name="unit_category_${i}" id="unit_category"
                //                            placeholder="请输入">
                //                 </div>
                //             </div>
                //             <div class="form-group">
                //                 <label for="social_num" class="col-sm-6 control-label">统一社会信用代码</label>
                //                 <div class="col-sm-6">
                //                     <input type=" text" class="form-control" name="social_num_${i}"  id="social_num"
                //                            placeholder="请输入">
                //                 </div>
                //             </div>
                //             <div class="form-group">
                //                 <label for="org_num" class="col-sm-6 control-label">尚未领取统一社会信用代码的组织机构代码</label>
                //                 <div class="col-sm-6">
                //                     <input type=" text" class="form-control" name="org_num_${i}" id="org_num"
                //                            placeholder="请输入">
                //                 </div>
                //             </div>
                //             <div class="form-group">
                //                 <label for="name" class="col-sm-6 control-label">单位详细名称</label>
                //                 <div class="col-sm-6">
                //                     <input type=" text" class="form-control" name="name_${i}" id="name"
                //                            placeholder="请输入">
                //                 </div>
                //             </div>
                //             <div class="form-group">
                //                 <label for="address" class="col-sm-6 control-label">详细地址</label>
                //                 <div class="col-sm-6">
                //                     <input type=" text" class="form-control" name="address_${i}" id="address"
                //                            placeholder="请输入">
                //                 </div>
                //             </div>
                //             <div class="form-group">
                //                 <label for="zone_num" class="col-sm-6 control-label">区划代码（六位）</label>
                //                 <div class="col-sm-6">
                //                     <input type=" text" class="form-control" name="zone_num_${i}" id="zone_num"
                //                            placeholder="请输入">
                //                 </div>
                //             </div>
                //             <div class="form-group">
                //                 <label for="mobile" class="col-sm-6 control-label">联系电话</label>
                //                 <div class="col-sm-6">
                //                     <input type=" text" class="form-control" name="mobile_${i}" id="mobile"
                //                            placeholder="请输入">
                //                 </div>
                //             </div>
                //             <div class="form-group">
                //                 <label for="main_activity" class="col-sm-6 control-label">主要业务活动</label>
                //                 <div class="col-sm-6">
                //                     <input type=" text" class="form-control" name="main_activity_${i}" id="main_activity"
                //                            placeholder="请输入">
                //                 </div>
                //             </div>
                //             <div class="form-group">
                //                 <label for="catrgory_code" class="col-sm-6 control-label">行业代码（小类 GB/T4754-2017）</label>
                //                 <div class="col-sm-6">
                //                     <input type=" text" class="form-control" name="catrgory_code_${i}"  id="catrgory_code"
                //                            placeholder="请输入">
                //                 </div>
                //             </div>
                //             <div class="form-group">
                //                 <label for="incumbency_num" class="col-sm-6 control-label">从业人员期末人数（人数）</label>
                //                 <div class="col-sm-6">
                //                     <input type=" text" class="form-control" name="incumbency_num_${i}" id="incumbency_num"
                //                            placeholder="请输入">
                //                 </div>
                //             </div>
                //             <div class="form-group">
                //                 <label for="manage_income" class="col-sm-6 control-label">经营性单位收入（元）</label>
                //                 <div class="col-sm-6">
                //                     <input type=" text" class="form-control" name="manage_income_${i}"  id="manage_income"
                //                            placeholder="请输入">
                //                 </div>
                //             </div>
                //             <div class="form-group">
                //                 <label for="inmanage_pay" class="col-sm-6 control-label">非经营性单位支出（费用/元）</label>
                //                 <div class="col-sm-6">
                //                     <input type=" text" class="form-control" name="inmanage_pay_${i}" id="inmanage_pay"
                //                            placeholder="请输入">
                //                 </div>
                //             </div>
                //         </div>
                // </div>
                // `
            // )
        }




    });

})