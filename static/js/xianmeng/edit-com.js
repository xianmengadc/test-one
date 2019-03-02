$(document).ready(function () {


    var data = $("#base_form").serializeArray();
    var postData = {};
    for (var x in data) {
        postData[data[x].name] = data[x].value;
    }
    console.log(postData.profess_category)
    if (postData.comp_type == '1') {
        $(".card-c").show();
        $(".card-d").hide();
    }
    if (postData.comp_type == '2') {
        $(".card-c").hide();
        $(".card-d").show();
    }

    if (postData.is_piling == '1') {
        $(".card-b").show();
    }
    if (postData.is_piling == '2') {
        $(".card-b").hide();
    }

    if (postData.is_higher_legal == '1') {
        $(".legal-unite").show();
    }
    if (postData.is_higher_legal == '0') {
        $(".legal-unite").hide();
    }
    //如果是当年注销企业 隐藏后续表单
    if (postData.operate_status == '6') {
        $(".operate-status-hide").hide();
    } else {
        $(".operate-status-hide").show();
    }
    $("#operate_status").change(function () {
        var selected = $(this).children('option:selected').val()
        if (selected == '6') {
            $(".operate-status-hide").hide();
        } else {
            $(".operate-status-hide").show();
        }
    });
    //如果是当年注销企业 隐藏后续表单
    $("input:radio[name='comp_type']").change(function () { //获取单位类型 1 法人单位  2 产业活动单位
        if (this.value == 1) {
            toastr.info("已选择法人单位");
            $(".card-c").show();
            $(".card-d").hide();
        }
        if (this.value == 2) {
            toastr.info("已选择产业活动单位");
            $(".card-c").hide();
            $(".card-d").show();
        }
    });

    $("input:radio[name='is_piling']").change(function () { //获取批发零售住宿餐饮状态 1 是  2 不是
        if (this.value == 1) {
            $(".card-b").show();
        }
        if (this.value == 2) {
            $(".card-b").hide();
        }
    });
    $("input:radio[name='is_higher_legal']").change(function () {
        if (this.value == 1) {
            toastr.info("本法人单位有上一级法人");
            $(".legal-unite").show();

        }
        if (this.value == 0) {
            toastr.info("本法人单位无上一级法人");
            $(".legal-unite").hide();
        }

    });

    //表单提交
    // $("#frm").submit();
    $("#onClickButton").click(function () {
            // 统一社会信用代码和组织机构代码必填一个
            if ($("#social_num")[0].value == '' && $("#org_num")[0].value == '') {
                toastr.error("统一社会信用代码和组织机构代码不能都为空，必须填一个");
                return false
            }
            console.log($("#social_num")[0].value.length)
            if ($("#social_num")[0].value != '' && $("#social_num")[0].value.length != 18) {
                toastr.error("统一社会信用代码必须为18位。");
                return false
            }
            var data = $("#base_form").serializeArray();
            var postData = {};


            for (var x in data) {
                postData[data[x].name] = data[x].value;
            }

            console.log(postData.address)
            if (postData.comp_type == undefined) {
                toastr.error("单位类型未填写");
                return false
            }


            //A块

            if (postData.name == '') {
                toastr.error("单位详细名称未填写");
                return false
            }
            if (postData.legal_person == '') {
                toastr.error("法定代表人（单位负责人）未填写");
                return false
            }
            if (postData.est_year == '') {
                toastr.error("开业（成立）时间--年未填写");
                return false
            }
            if (postData.est_month == '') {
                toastr.error("开业（成立）时间--月未填写");
                return false
            }
            // if (postData.landline_area_code == '') {
            //     toastr.error("长途区号未填写");
            //     return false
            // }
            // if (postData.landline_num == '') {
            //     toastr.error("固定电话未填写");
            //     return false
            // }

            if (postData.province == '') {
                toastr.error(" 单位所在地及区划 省 未填写");
                return false
            }
            // console.log( $("input:radio[name='is_piling']"))

            var operate_type = $('#retail_opetrate_type').val();
            var data = $("#base_form").serializeArray();
            var postData = {};

            // console.log(data);

            // console.log(postData.register_type);
            for (var x in data) {
                if ((data[x].name == 'retail_opetrate_type' && data[x].name != '') || (data[x].name == 'legal_unite_hkmatai' && data[x].name != '')) {
                    postData[data[x].name] = postData[data[x].name] + ',' + data[x].value;
                } else {
                    postData[data[x].name] = data[x].value;
                }


            }

            // console.log(postData.retail_opetrate_type);
            // console.log(postData.legal_unite_hkmatai);
            // console.log(111111111)
            // return false
            if (postData.retail_opetrate_type == undefined) {
                postData.retail_opetrate_type = ''
            } else {
                postData.retail_opetrate_type = postData.retail_opetrate_type.substring(10)
            }
            if (postData.legal_unite_hkmatai == undefined) {
                postData.legal_unite_hkmatai = ''
            } else {
                postData.legal_unite_hkmatai = postData.legal_unite_hkmatai.substring(10)
            }

            // postData.retail_opetrate_type = postData.retail_opetrate_type.substring(10)
            // postData.legal_unite_hkmatai = postData.legal_unite_hkmatai.substring(10)
            // console.log(postData.legal_unite_hkmatai);
            //专业类别判断条件
            // if (postData.profess_category == 'X' && postData.branch_comp_house_sale_area == '') {
            //     toastr.error("专业类别为房地产开发经营业必须填写197项");
            //     return false
            // }


            if (postData.city == '') {
                toastr.error("单位所在地及区划 市 未填写");
                return false
            }
            if (postData.interviewee == '') {
                toastr.error("申报人 未填写");
                return false
            }
            if (postData.interviewee_contact == '') {
                toastr.error("申报人联系电话 未填写");
                return false
            }

            if (postData.district == '') {
                toastr.error("单位所在地及区划 区 未填写");
                return false
            }
            if (postData.address == '') {
                toastr.error("单位所在地及区划 区 未填写");
                return false
            }
            if (postData.profess_category == 'C') {
                if (postData.register_province == '') {
                    toastr.error("单位注册地及区划 省 未填写");

                    postData.retail_opetrate_type = operate_type;
                    console.log(postData)
                }
                if (postData.register_city == '') {
                    toastr.error("单位注册地及区划 市 未填写");
                    return false
                }
                if (postData.register_district == '') {
                    toastr.error("单位注册地及区划 区 未填写");
                    return false
                }
                if (postData.register_address == '') {
                    toastr.error("单位注册地及区划 街道 未填写");
                    return false
                }
            }
            //A块
            if (postData.comp_type == '1') {
                // if (postData.org_type == 10 && postData.accounting_rule != 1) {
                //     $("#accounting_rule").parent().parent().addClass("has-error")
                //     toastr.error("机构类型和执行会计标准类别不匹配！！！");
                //     return false
                // }
                // if (postData.org_type == '20' && (postData.accounting_rule == '3' || postData.accounting_rule == '4' || postData.accounting_rule == '9')) {
                //     $("#accounting_rule").parent().parent().addClass("has-error")
                //     toastr.error("机构类型和执行会计标准类别不匹配！！！");
                //     return false
                // }
                // if (postData.org_type == '30' && postData.accounting_rule != '3') {
                //     $("#accounting_rule").parent().parent().addClass("has-error")
                //     toastr.error("机构类型和执行会计标准类别不匹配！！！");
                //     return false
                // }
                // if (postData.org_type != '30' && postData.accounting_rule == '3') {
                //     $("#accounting_rule").parent().parent().addClass("has-error")
                //     toastr.error("机构类型和执行会计标准类别不匹配！！！");
                //     return false
                // }
                // if (postData.org_type == '10' && postData.legal_unite_hypotaxis != '90') {
                //     toastr.error("机构类型是企业的隶属关系只能选其他");
                //     return false
                // }

            }
            if (postData.operate_status == undefined) {
                toastr.error("运营状态 未填写");
                return false
            }
            if (postData.landline_area_code != '' && postData.landline_num == '') {
                toastr.error("203区号或者固定电话 未填写");
                return false
            }
            if (postData.landline_area_code == '' && postData.landline_num != '') {
                toastr.error("203区号或者固定电话 未填写");
                return false
            }
            if (postData.mobile == '' && postData.landline_num == '') {
                toastr.error("203移动电话 固定电话 必须填一个");
                return false
            }
            if (postData.mobile != '' && postData.mobile.length != 11) {
                toastr.error("203移动电话必须是11位");
                return false
            }
            // if (postData.postalcode == '') {
            //     toastr.error("邮政编码 未填写");
            //     return false
            // }
            if (postData.operate_status != '6') {
                if (postData.main_activity_1 == '') {
                    toastr.error("主要业务活动 未填写");
                    return false
                }
                if (postData.org_type == undefined) {
                    toastr.error("机构类型 未填写");
                    return false
                }
                if (postData.register_type == undefined) {
                    toastr.error("登记注册类型 未填写");
                    return false
                }

                if (postData.is_piling == undefined) {
                    toastr.error("是否为批发、零售、住宿或者餐饮法人或产业活动单位未填写");
                    return false
                }


                //B板块
                //是批发零售住宿餐饮法人单位或产业活动单位认证
                if (postData.is_piling == '1') {

                    //主要业务活动 main_activity_1
                    var reg = RegExp(/批发/);
                    if (reg.test(postData.main_activity_1 && postData.retail_management_form != '1')) {
                        toastr.error("主要业务活动中还有'批发',ES1必选1");
                        return false
                    }

                    if (postData.retail_management_form == undefined) {
                        toastr.error("批发和零售业、住宿和餐饮业单位经营形式 未填写");
                        return false
                    }


                    if (postData.retail_management_form == '2' || postData.retail_management_form == '3' || postData.retail_management_form == '4') {
                        if (postData.retail_management_brand == undefined) {
                            toastr.error("连锁品牌（商标或者商号名称） 未填写");
                            return false
                        }
                    }


                }

                //C板块
                if (postData.comp_type == '1') {

                    //审核205
                    if (postData.register_type == '171' || postData.register_type == '172' || postData.register_type == '173' || postData.register_type == '174') {
                        if (postData.legal_unite_stake != '3') {
                            toastr.error("205登记注册类型与206企业控股情况不相匹配");
                            return false
                        }
                    }
                    if (postData.register_type == '210' || postData.register_type == '290' || postData.register_type == '220' || postData.register_type == '230' || postData.register_type == '240') {
                        if (postData.legal_unite_hkmatai == '') {
                            toastr.error("216 港澳台投资情况必填");
                            return false
                        }
                    }


                    if (postData.legal_unite_hypotaxis == undefined) {
                        toastr.error("C板块 隶属关系 未填写");
                        return false
                    }
                    if (postData.legal_unite_stake == undefined) {
                        toastr.error("C板块 企业控股情况 未填写");
                        return false
                    }
                    if (postData.accounting_rule == undefined) {
                        toastr.error("C板块 执行会计标准情况 未填写");
                        return false
                    }
                    if (postData.is_higher_legal == undefined) {
                        toastr.error("C板块 本法人单位是否有上一级法人 未填写");
                        return false
                    }
                    if (postData.is_higher_legal == '1') {
                        if (postData.legal_unite_social_num == '' && postData.legal_unite_org_num == '') {
                            toastr.error("C板块 上一级法人统一社会信用代码和组织机构代码 必须填写一个");
                            return false
                        }
                        if (postData.legal_unite_social_num != '' && postData.legal_unite_social_num.length != 18) {
                            toastr.error("C板块 上一级法人统一社会信用代码必须为18位");
                            return false
                        }
                        if (postData.legal_unite_name == '') {
                            toastr.error("C板块 上一级法人单位详细名称 未填写");
                            return false
                        }
                    }

                    if (postData.has_branch == undefined) {
                        toastr.error("C板块 本法人单位是否有下属产业活动单位 未填写");
                        return false
                    }

                    console.log(111111112323213)
                    console.log(postData.legal_unite_accounting_standard)
                    if (postData.accounting_rule != '1' && postData.legal_unite_accounting_standard != '0') {
                        toastr.error("(209)不执行企业会计制度的不填（210）");
                        return false
                    }
                }

                //产业活动单位D 认证
                if (postData.comp_type == '2') {
                    if (postData.parent_type == undefined) {
                        toastr.error("D板块 产业活动单位归属法人单位情况必须填报！！！");
                        return false
                    }
                    if (postData.parent_comp_social_num == '' && postData.parent_comp_org_num == '') {
                        toastr.error("D板块 法人单位统一社会信用代码或者组织机构代码必须填报一个！！！");
                        return false
                    }
                    if (postData.parent_comp_social_num != '' && postData.parent_comp_social_num.length != 18) {
                        toastr.error("D板块 法人单位统一社会信用代码必须为18位！！！");
                        return false
                    }

                    if (postData.parent_comp_name == '') {
                        toastr.error("D板块 法人单位详细名称必须填报！！！");
                        return false
                    }
                    if (postData.parent_comp_address == '') {
                        toastr.error("D板块 法人单位详细地址必须填报！！！");
                        return false
                    }
                    if (postData.branch_comp_count_obtainemploy == '') {
                        toastr.error("D板块 从业人员期末人数必须填报！！！");
                        return false
                    }
                    if (parseInt(postData.branch_comp_count_obtainemploy) <= 0) {
                        toastr.error("D板块 从业人员期末人数必须为正数！！！");
                        return false
                    }
                    if (postData.branch_comp_count_obtainemploy_female == '') {
                        toastr.error("D板块 其中：女性必须填报！！！");
                        return false
                    } else if (parseInt(postData.branch_comp_count_obtainemploy) < parseInt(postData.branch_comp_count_obtainemploy_female)) {
                        toastr.error("D板块 从业人员期末人数必须大于女性人数！！！");
                        return false
                    }


                    if (postData.branch_comp_nooperate_defray != '' && postData.branch_comp_operate_income != '') {
                        toastr.error("D板块 非经营性单位收入和经营性单位收入不能同时填报！！！");
                        return false
                    }
                    if (postData.branch_comp_nooperate_defray != '') {
                        if (parseInt(postData.branch_comp_nooperate_defray) < 0) {
                            toastr.error("D板块 非经营性单位收入必须大于等于0！！！");
                            return false
                        }
                    }
                    if (postData.branch_comp_operate_income != '') {
                        if (parseInt(postData.branch_comp_operate_income) < 0) {
                            toastr.error("D板块 经营性单位收入必须大于等于0！！！");
                            return false
                        }
                    }

                    if (parseInt(postData.branch_comp_house_sale_area) < 0) {
                        toastr.error("D板块 本年商品房销售面积必须大于等于0！！！");
                        return false
                    }
                    if (parseInt(postData.branch_comp_house_sale_area) < 0) {
                        toastr.error("D板块 年末商品房待售面积必须大于等于0！！！");
                        return false
                    }

                }
            }


            var cid = $("#cid").val();
            var next_url = '/edit_611_1/' + cid;
            console.log(postData.street_district)
            $.post('/edit_com/' + postData.street_district + '/' + cid + '/?next=' + next_url, postData, function (res) {

                for (var msg1 in res.msg) {
                    // console.log(msg1 + "," + res.msg[msg1])
                }

                // console.log(res);

                if (res.code == 0) {
                    toastr.success("保存成功");
                    window.setTimeout(function () {
                        window.location.replace('/edit_com/' + postData.street_district + '/' + res.next + '/')
                    }, 1000);
                } else {
                    for (var msg1 in res.msg) {
                        toastr.error(msg1 + "," + res.msg[msg1]);
                    }
                }
            }).fail(function (jqXHR, textStatus, errorThrown) {
                toastr.error('提交失败请稍后重试');
            });
            return false;


        }
    )


})