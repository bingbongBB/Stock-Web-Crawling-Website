$(document).ready(function(){
	let stock_codes = ['1301','1303','2317','2330','2412','2454','2603','2881','2882','6505'];
	$('#searcholddata').click(function(){
		let stock_code = $("#stockid").val();
		let year = $("#year").val();
		let month = $("#month").val();
		if (stock_code == "" || year=="" || month == ""){
			alert("請勿空值");
		}else{
			if (!stock_codes.includes(stock_code) || !Number(year) || !Number(month)){
				alert("請輸入正確格式");
			}else{
				if (year.length!=4 || Number(month)>12 || Number(month) < 1){
					alert("請輸入正確時間範圍");
				}
				else{
					if (month.length == 1){
						month = "0"+month;
					}
					window.location = "stockhistory/"+stock_code+"/"+year+"/"+month;			
				}
			}
		}
	});
});
