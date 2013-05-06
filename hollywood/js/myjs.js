function do_visual(company)
{	
	$.post('/do_viz',{'viz':company}, function(data) {
		
		// *************************************************************************
		$(function () {
		        $('#viz-area1').highcharts({
		            chart: {
		                type: 'column'
		            },
		            title: {
		                text: 'Genre films statistics'
		            },
		            subtitle: {
		                text: 'Source: IMDB'
		            },
		            xAxis: {
		                categories: data.genres_name1
		            },
		            yAxis: {
		                min: 0,
		                title: {
		                    text: 'Number'
		                }
		            },
		            tooltip: {
		                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		                    '<td style="padding:0"><b>{point.y:.1f} </b></td></tr>',
		                footerFormat: '</table>',
		                shared: true,
		                useHTML: true
		            },
		            plotOptions: {
		                column: {
		                    pointPadding: 0.2,
		                    borderWidth: 0
		                }
		            },
		            series: [{
		                name: 'film number',
		                data: data.genre_count

		            }]
		        });
		    });
		// *************************************************************************
		$(function () {
		        $('#viz-area2').highcharts({
		            chart: {
		                type: 'column'
		            },
		            title: {
		                text: 'Genre average gross statistics'
		            },
		            subtitle: {
		                text: 'Source: IMDB'
		            },
		            xAxis: {
		                categories: data.genres_name2
		            },
		            yAxis: {
		                min: 0,
		                title: {
		                    text: 'average gross (Millions)'
		                }
		            },
		            tooltip: {
		                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		                    '<td style="padding:0"><b>{point.y:.1f} </b></td></tr>',
		                footerFormat: '</table>',
		                shared: true,
		                useHTML: true
		            },
		            plotOptions: {
		                column: {
		                    pointPadding: 0.2,
		                    borderWidth: 0
		                }
		            },
		            series: [{
		                name: 'average gross',
		                data: data.genre_count2,
						color: "green"

		            }]
		        });
		    });
		
		
			// *************************************************************************
			// *************************************************************************
			// $(function () {
			//         $('#viz-area3').highcharts({
			//             chart: {
			//                 type: 'column'
			//             },
			//             title: {
			//                 text: 'youtube likes statistics'
			//             },
			//             subtitle: {
			//                 text: 'Source: Youtube'
			//             },
			//             xAxis: {
			//                 categories: data.genres_name3
			//             },
			//             yAxis: {
			//                 min: 0,
			//                 title: {
			//                     text: 'like percentage'
			//                 }
			//             },
			//             tooltip: {
			//                 headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
			//                 pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
			//                     '<td style="padding:0"><b>{point.y:.1f} </b></td></tr>',
			//                 footerFormat: '</table>',
			//                 shared: true,
			//                 useHTML: true
			//             },
			//             plotOptions: {
			//                 column: {
			//                     pointPadding: 0.2,
			//                     borderWidth: 0
			//                 }
			//             },
			//             series: [{
			//                 name: '',
			//                 data: data.genre_count3,
			// 				color: "purple"
			// 
			//             }]
			//         });
			//     });


				// *************************************************************************
				// *************************************************************************	
				$(function () {
				        $('#side1').highcharts({
				            chart: {
				                type: 'bar'
				            },
				            title: {
				                text: 'Top gross film'
				            },
				            subtitle: {
				                text: 'Source: IMDB'
				            },
				            xAxis: {
				                categories: data.top_gross,
				                title: {
				                    text: null
				                }
				            },
				            yAxis: {
				                min: 0,
				                title: {
				                    text: '(millions)',
				                    align: 'high'
				                },
				                labels: {
				                    overflow: 'justify'
				                }
				            },
				            tooltip: {
				                valueSuffix: ' millions'
				            },
				            plotOptions: {
				                bar: {
				                    dataLabels: {
				                        enabled: true
				                    },
								color:"red"
				                }
				            },
				            legend: {
				                layout: 'vertical',
				                align: 'right',
				                verticalAlign: 'top',
				                x: -100,
				                y: 100,
				                floating: true,
				                borderWidth: 1,
				                backgroundColor: '#FFFFFF',
				                shadow: true
				            },
				            credits: {
				                enabled: false
				            },
				            series: [{
				                name: 'gross',
				                data: data.top_gross_value
				            }]
				        });
				    });
			// *************************************************************************
			// *************************************************************************
				$(function () {
				        $('#side2').highcharts({
				            chart: {
				                type: 'bar'
				            },
				            title: {
				                text: 'Top rating film'
				            },
				            subtitle: {
				                text: 'Source: rotton tomato (audience)'
				            },
				            xAxis: {
				                categories: data.top_rating,
				                title: {
				                    text: null
				                }
				            },
				            yAxis: {
				                min: 0,
				                title: {
				                    text: '(score)',
				                    align: 'high'
				                },
				                labels: {
				                    overflow: 'justify'
				                }
				            },
				            plotOptions: {
				                bar: {
				                    dataLabels: {
				                        enabled: true
				                    },
								color:"pink"
				                }
				            },
				            legend: {
				                layout: 'vertical',
				                align: 'right',
				                verticalAlign: 'top',
				                x: -100,
				                y: 100,
				                floating: true,
				                borderWidth: 1,
				                backgroundColor: '#FFFFFF',
				                shadow: true
				            },
				            credits: {
				                enabled: false
				            },
				            series: [{
				                name: 'score',
				                data: data.top_rating_score
				            }]
				        });
				    });
			// *************************************************************************
			// *************************************************************************
				$(function () {
				        $('#side3').highcharts({
				            chart: {
				                type: 'bar'
				            },
				            title: {
				                text: 'Top Trailer views film'
				            },
				            subtitle: {
				                text: 'Source: youtube'
				            },
				            xAxis: {
				                categories: data.top_views,
				                title: {
				                    text: null
				                }
				            },
				            yAxis: {
				                min: 0,
				                title: {
				                    text: '(million times)',
				                    align: 'high'
				                },
				                labels: {
				                    overflow: 'justify'
				                }
				            },
				            tooltip: {
				                valueSuffix: ' million times'
				            },
				            plotOptions: {
				                bar: {
				                    dataLabels: {
				                        enabled: true
				                    },
								color:"orange"
				                }
				            },
				            legend: {
				                layout: 'vertical',
				                align: 'right',
				                verticalAlign: 'top',
				                x: -100,
				                y: 100,
				                floating: true,
				                borderWidth: 1,
				                backgroundColor: '#FFFFFF',
				                shadow: true
				            },
				            credits: {
				                enabled: false
				            },
				            series: [{
				                name: 'click',
				                data: data.top_views_time
				            }]
				        });
				    });
			// *************************************************************************
			// *************************************************************************
			$(function () {
			        $('#viz-area3').highcharts({
			            chart: {
			                type: 'column'
			            },
			            title: {
			                text: 'Percentage of positive reviews'
			            },
			            subtitle: {
			                text: 'Source: RottonTomato'
			            },
			            xAxis: {
			                categories: data.genres_name4
			            },
			            yAxis: {
			                min: 0,
			                title: {
			                    text: 'Critics and Audience Percentage of positive reviews'
			                }
			            },
			            tooltip: {
			                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
			                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
			                    '<td style="padding:0"><b>{point.y:.1f} </b></td></tr>',
			                footerFormat: '</table>',
			                shared: true,
			                useHTML: true
			            },
			            plotOptions: {
			                column: {
			                    pointPadding: 0.2,
			                    borderWidth: 0
			                }
			            },
			            series: [{
			                name: 'Critics',
			                data: data.ratings

			            }, {
			                name: 'Audience',
			                data: data.ratings2

			            }]
			        });
			    });	
				// *************************************************************************
				// *************************************************************************
				$(function () {
				        $('#viz-area4').highcharts({
				            chart: {
				                type: 'line',
				                marginRight: 130,
				                marginBottom: 25
				            },
				            title: {
				                text: 'Best Genre Monthly average Gross',
				                x: -20 //center
				            },
				            subtitle: {
				                text: 'Source: IMDB',
				                x: -20
				            },
				            xAxis: {
				                categories: data.months
				            },
				            yAxis: {
				                title: {
				                    text: 'Average Gross ($)'
				                },
				                plotLines: [{
				                    value: 0,
				                    width: 1,
				                    color: '#808080'
				                }]
				            },
				            tooltip: {
				                valueSuffix: '$'
				            },
				            legend: {
				                layout: 'vertical',
				                align: 'right',
				                verticalAlign: 'top',
				                x: -10,
				                y: 100,
				                borderWidth: 0
				            },
				            series: [{
				                name: data.g1,
				                data: data.month_gross1
				            },
							{
								 name: data.g2,
					             data: data.month_gross2
							},	{
					                name: data.g3,
					                data: data.month_gross3
					        }]
				        });
				    });
					$(function () {
					        $('#viz-area5').highcharts({
					            chart: {
					                type: 'line',
					                marginRight: 130,
					                marginBottom: 25
					            },
					            title: {
					                text: 'Best Genre Monthly average Gross',
					                x: -20 //center
					            },
					            subtitle: {
					                text: 'Source: IMDB',
					                x: -20
					            },
					            xAxis: {
					                categories: data.months
					            },
					            yAxis: {
					                title: {
					                    text: 'Average Gross ($)'
					                },
					                plotLines: [{
					                    value: 0,
					                    width: 1,
					                    color: '#808080'
					                }]
					            },
					            tooltip: {
					                valueSuffix: '$'
					            },
					            legend: {
					                layout: 'vertical',
					                align: 'right',
					                verticalAlign: 'top',
					                x: -10,
					                y: 100,
					                borderWidth: 0
					            },
					            series: [{
					                name: data.g1,
					                data: data.month_gross1
					            }]
					        });
					    });		
							
		
	},"json");	
}

function refresh_1() {
	

	var year=$("#refresh_1").val();
	var genre=$("#refresh_2").val();
	var page = $("#page").text();
	
	$.post('/refresh',{'company':page,'year':year,'genre':genre}, function(data) {
		$(function () {
		        $('#viz-area5').highcharts({
		            chart: {
		                type: 'line',
		                marginRight: 130,
		                marginBottom: 25
		            },
		            title: {
		                text: 'Selected Year and Genre Monthly average Gross',
		                x: -20 //center
		            },
		            subtitle: {
		                text: 'Source: IMDB',
		                x: -20
		            },
		            xAxis: {
		                categories: data.months
		            },
		            yAxis: {
		                title: {
		                    text: 'Average Gross ($)'
		                },
		                plotLines: [{
		                    value: 0,
		                    width: 1,
		                    color: '#808080'
		                }]
		            },
		            tooltip: {
		                valueSuffix: '$'
		            },
		            legend: {
		                layout: 'vertical',
		                align: 'right',
		                verticalAlign: 'top',
		                x: -10,
		                y: 100,
		                borderWidth: 0
		            },
		            series: [{
		                name: data.g1,
		                data: data.month_gross1
		            }]
		        });
		    });
		
	},"json");	
};