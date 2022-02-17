var Gpio = require('onoff').Gpio; //include onoff to interact with the GPIO
var Led = new Gpio(20, 'out'); 
var Button = new Gpio(19, 'in'); 

function ledControl() {

    if (Button.readSync() === 0) {
        LED.writeSync(1); //set pin state to 1 (turn LED on)
    }
    else {
        LED.writeSync(0); //set pin state to 0 (turn LED off)
    }
}


ledControl()


var Gpio = require('onoff').Gpio; //include onoff to interact with the GPIO
var LED = new Gpio(20, 'out'); //use GPIO pin 20 as output
var pushButton = new Gpio(19, 'in', 'both'); //use GPIO pin 19 as input, and 'both' button presses, and releases should be handled

pushButton.watch(function (err, value) { //Watch for hardware interrupts on pushButton GPIO, specify callback function
  if (err) { //if an error
    console.error('There was an error', err); //output error message to console
  return;
  }
  LED.writeSync(value); //turn LED on or off depending on the button state (0 or 1)
});

function unexportOnClose() { //function to run when exiting program
  LED.writeSync(0); // Turn LED off
  LED.unexport(); // Unexport LED GPIO to free resources
  pushButton.unexport(); // Unexport Button GPIO to free resources
};

process.on('SIGINT', unexportOnClose); //function to run when user closes using ctrl+c