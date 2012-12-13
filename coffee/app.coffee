
socket = new Socket("localhost:5000", []);

socket.on("nadeko", ->
	console.log("Nadeko");
);

scoket.on("cute", ->
	console.log("cute");
);

