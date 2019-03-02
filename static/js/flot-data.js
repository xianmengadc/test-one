// //Flot Line Chart
// $(document).ready(function() {
//     console.log("document ready");
//     var offset = 0;

// });



// // 普查底册柱状图

//     $(function() {
//         //some data
//         var d1 = [];
//         for (var i = 0; i <= 7; i += 1)
//             d1.push([i, parseInt(Math.random() * 60)]);

//         var d2 = [];
//         for (var i = 0; i <= 7; i += 1)
//             d2.push([i, parseInt(Math.random() * 40)]);

//         var d3 = [];
//         for (var i = 0; i <= 7; i += 1)
//             d3.push([i, parseInt(Math.random() * 25)]);

//         var ds = new Array();

//         ds.push({
//             label : "已通知",
//             data : d1,
//             bars : {
//                 order : 1
//             }
//         });
//         ds.push({
//             label : "未通知",
//             data : d2,
//             bars : {
//                 order : 2
//             }
//         });
//         ds.push({
//             label : "今日通知",
//             data : d3,
//             bars : {
//                 order : 3
//             }
//         });

//         var stack = 0,
//             bars = true,
//             lines = true,
//             steps = true;

//         var options = {
//             bars : {
//                 show : true,
//                 barWidth : 0.2,
//                 fill : 1
//             },
//             grid : {
//                 show : false,
//                 aboveData : false,
//                 labelMargin : 5,
//                 axisMargin : 0,
//                 borderWidth : 1,
//                 minBorderMargin : 5,
//                 clickable : true,
//                 hoverable : true,
//                 autoHighlight : false,
//                 mouseActiveRadius : 20,
//                 borderColor : '#f5f5f5'
//             },
//             series : {
//                 stack : stack
//             },
//             legend : {
//                 position : "ne",
//                 margin : [0, 0],
//                 noColumns : 0,
//                 labelBoxBorderColor : null,
//                 labelFormatter : function(label, series) {
//                     // just add some space to labes
//                     return '' + label + '&nbsp;&nbsp;';
//                 },
//                 width : 30,
//                 height : 5
//             },
//             yaxis : {
//                 tickColor : '#f5f5f5',
//                 font : {
//                     color : '#bdbdbd'
//                 }
//             },
//             xaxis : {
//                 tickColor : '#f5f5f5',
//                 ticks:[
//                     [ 0,'南院门'],
//                     [ 1,'柏树林'],
//                     [ 2,'长乐坊'],
//                     [ 3,'东关南'],
//                     [ 4,'太乙路'],
//                     [ 5,'文艺路'],
//                     [ 6,'长安路'],
//                     [ 7,'张家村'],
//                 ],
//                 font : {
//                     color : '#bdbdbd'
//                 }
//             },
//             colors : ["#4F5467", "#01c0c8", "#fb9678"],
//             tooltip : true, //activate tooltip
//             tooltipOpts : {
//                 content : "%s : %y.0",
//                 shifts : {
//                     x : -30,
//                     y : -50
//                 }
//             }
//         };

//         $.plot($(".sales-bars-chart"), ds, options);
//     });


