
class Socket
	constructor: (@url, @protocol) ->
		@connection = new WebSocket(@url, @protocol);
		@event = {};
		@connection.onopen = @onopen;
		@connection.onclose = @onclose;
		@connection.onmessage = @onmessage;

	on: (event_name, callback) ->
		@event[event_name] = callback;
	
	onmessage: (message) ->
		data = message.data;
		d = data.split(":"); #message format: event_name:args(json_encoding)
		event_name = d[0];
		json = d[1];
		args = eval("(" + json + ")");
		@event[event_name].apply(null, args);
	onopen: ->
		console.log("open");
	onclose: ->
		console.log("close");
	
