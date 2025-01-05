$(document).ready(function(){
	$('#searchnowdata').click(function(){
		let stock_code = $("#stockid").val();
		if (stock_code == ""){
			alert("請勿空值");
		}else{
			if (!Number(stock_code) || stock_code.length !=4){
				alert("請輸入正確格式");
			}else{
				$.ajax({
					url: '/realtime/',
					async  : 'True',
					type: 'POST',
					data: {'stock_code': stock_code},
				}).done(function(msg) {
					let html = "";
					for(let i = 0;i<msg.best_bid_price.length;i++){
						html += "<tr>";
						html += "<td>" + msg.best_bid_price[i] +"</td>";
						html += "<td>" + msg.best_bid_volume[i] +"</td>";
						html += "<td>" + msg.best_ask_price[i] +"</td>";
						html += "<td>" + msg.best_ask_volume[i] +"</td>";
						html += "</tr>";
					}
					$("#searchdate").html(msg.date);
					$("#stockname").html(msg.name);
					$("#stockid").html(msg.code);
					$("#stockfullname").html(msg.fullname);

					$("#st").html(html);
					$("#openprice").html(msg.open);
					$("#highestpri").html(msg.high);
					$("#lowestpri").html(msg.low);
				});	
			}
		}
	});
});
