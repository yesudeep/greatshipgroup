
function tableToData(id){
    var data = {
        labelsXAxis: [],
        labelsYAxis: [],
        plotData: []
    },
    rows = jQuery(id).find('tr');
    
    for (var i = 0, rowsCount = rows.length; i < rowsCount; ++i){
        var row = jQuery(rows[i]), 
            cells = row.find('td'),
            //xLabel = jQuery(row.find('th')[0]).text(),
            yLabel = jQuery(row.find('th')[0]).text(), 
            datum = {
                label: yLabel,
                data: []
            };
        data.labelsYAxis.push(yLabel);
        if (i > 0){         
            for (var j = 0, cellsCount = cells.length; j < cellsCount; ++j){
                var value = jQuery.trim(jQuery(cells[j]).text());
                if (value === ""){
                    value = 0;
                }
                datum.data.push(value);
            }
            data.plotData.push(datum);
        } else {
            for (var j = 0, cellsCount = cells.length; j < cellsCount; ++j){
                var value = jQuery(cells[j]).text();
                data.labelsXAxis.push(value);
            }
        }
        
    }
    return data;
}


function convertToSeries(data){
    var series = [];
    var colors = [
        'fce94f',
        'fcaf3e',
        'e9b96e',
        '8ae234',
        '729fcf',
        'ad7fa8',
        'ef2929',
        'edd400',
        'f57900',
        'c17d11',
        '73d216',
        '3465a4',
        '75507b',
        'cc0000',
        'c4a000',
        'cefc00',
        '8f5902',
        '4e9a06',
        '204a87',
        '5c3566',
        'a40000'
    ];
    for (var i = 0, datum={}, len=data.plotData.length; i < len; i++){
        datum = data.plotData[i];
        series.push(jQuery.gchart.series(datum.label, datum.data, colors.shift()));
    }
    return series;
}

jQuery(function(){
   var incomeStatement = tableToData('#income-statement'),
        assetLiabilityStatement = tableToData('#asset-liability-statement');
        
   jQuery('#income-statement-chart').gchart({
       type: 'line',
       dataLabels: incomeStatement.labelsXAxis,
       legend: 'right',
       series: convertToSeries(incomeStatement)
   });
   jQuery('#asset-liability-statement-chart').gchart({
       type: 'line',
       dataLabels: assetLiabilityStatement.labelsXAxis,
       legend: 'right',
       series: convertToSeries(assetLiabilityStatement)
   });

});

/*
jQuery(function(){

    var income_statement_data = tableToData('#income-statement');
    var xAxis = [0];
    for (var i = 0; i < income_statement_data.labelsXAxis.length; i++){
        xAxis.push([i + 1, income_statement_data.labelsXAxis[i]]);
    }
    var yAxis = [0];
    for (var i = 0; i < income_statement_data.labelsYAxis.length; i++){
        yAxis.push([i + 1, income_statement_data.labelsYAxis[i]]);
    }
    var options = {
        legend: {
            show: true,
            margin: 10,
            backgroundOpacity: 0.5
        },
        points: {
            show: true,
            radius: 3
        },
        lines: {
            show: false
        },
        grid: {
            borderWidth:0
        },
        xaxis: {
            tickSize:1,
            ticks: xAxis
        },
        yaxis: {
            tickSize:10
            //tickDecimals: 0
        }
    };

    jQuery.plot(jQuery('#placeholder'), income_statement_data.plotData, options);    
});
*/