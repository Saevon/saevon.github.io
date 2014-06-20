function Sound(sampleRate) {
  this.sampleRate = sampleRate;

  this.data = [];
  this.append();

  this.finished = false;
}

/*
 * Add saves the current position, and any consequtive additions will
 * all be merged together then normalized
 *
 * add()
 *
 * add(null, pos)
 *    pos:  (optional) the position to start the add at
 *
 * add(list data, int pos)
 *    data: the list to add to the Sound
 *    post: (optional) the position to start the add at
 */
Sound.prototype.add = function(data, pos) {
  if (data === undefined || data === null) {
    if (pos !== undefined) {
      this.set_pos(pos);
    } else {
      this.pos = this.data.length;
    }
    this.mode = "add";
  } else {
    // Assertions
    // TODO: check that its a list
    if (pos !== undefined) {
      this.set_pos(pos);
    }

    // Now we merge in the data
    var end = this.pos;
    for (var i=0; i < data.length; i++) {
      // If we have space we merge, otherwise we add
      if ((this.pos + i) < this.data.length) {
        this.data[this.pos + i] += data[i];
        end = this.pos + i;
      } else {
        this.data.push(data[i]);
      }
    }

    // And finally we normalize the block
    this.normalize(this.pos, end);
  }

  return this;
};
/*
 * Sets the position to the given value
 *  Only makes sense in 'add' mode
 */
Sound.prototype.set_pos = function(pos) {
  // Assertions
  if (pos === undefined || pos < 0 || pos >= this.data.length) {throw Error("Invalid Position: " + pos);}

  this.pos = pos;

  return this;
};

/*
 * append()
 *    Sets the Sound to append all consequent datapoints
 *
 * append(list data)
 *    Appends to the Sound the given data list.
 */
Sound.prototype.append = function(data) {
  if (data === undefined) {
    this.mode = "append";
  } else {
    // Assertions
    // TODO: check that its a list

    // Now we copy over the data
    for (var i=0; i < data.length; i++) {
      this.data.push(data[i]);
    }
  }

  return this;
};

/*
 * Uses the given mode to push data into the Sound
 */
Sound.prototype.push = function(data) {
  // Assertions
  // TODO: ensure its a list

  // Now Send the data over
  if (this.mode == "add") {
    this.add(data);
  } else {
    this.append(data);
  }

  return this;
};


/*
 * Creates an array of values representing a musical tone of the given frequency
 *
 * freq:     frequency in hz
 * duration: length in seconds
 * offset:   (optional) since curve offset in seconds
 */
Sound.prototype.tone = function(freq, duration, offset) {
  // Assertions
  if (freq === undefined || freq <= 0) {throw "Invalid Frequency: " + freq;}
  if (duration === undefined || duration <= 0) {throw "Invalid Duration: " + duration;}

  // Optional Args
  // TODO: What about negative offsets?
  offset = (offset !== undefined) ? offset : 0;

  // Update the values to now use the store sampleRate
  duration *= this.sampleRate;
  offset *= this.sampleRate;

  // Update the data curve
  var curve = [];
  for (var i=0; i < duration; i++) {
    // Calculate the value of the sine curve at this position
    curve.push(
      Math.sin((2 * Math.PI) * freq * ((i + offset) / this.sampleRate))
    );
  }

  // Now add the data to the Sound
  this.push(curve);

  return this;
};

/*
 * Creates an array of values representing silence
 *
 * duration: length in seconds
 */
Sound.prototype.silence = function(duration) {
  // Assertions
  if (duration === undefined || duration <= 0) {throw "Invalid Duration: " + duration;}

  duration = this.sampleRate * duration;

  var curve = [];
  for (var i=0; i < duration; i++) {
    curve.push(0);
  }

  // Add the data
  this.push(curve);

  return this;
};


/*
 * Normalizes the tone to values between 1 and -1
 */
Sound.prototype.normalize = function(start, end) {
  // Assertions
  if (start === undefined || start < 0 || start >= this.data.length) {throw "Invalid Start: " + start;}
  if (end === undefined || end < 0 || end >= this.data.length) {throw "Invalid End: " + end;}

  // TODO: What about negative values?

  // We need to find the highest value
  var max = this.data.splice(start, end).reduce(function(val1, val2) {return Math.max(Math.abs(val1), Math.abs(val2));}, 0);

  // Now we can normalize
  for (var i=start; i < end; i++) {
    this.data[i] = this.data[i] / max;
  }
  console.log(this.data.splice(0,20));

  return this;
};


/*
 * Converts the tone into values between 0 to 255
 */
Sound.prototype._convert255 = function() {
  for (var i=0; i < this.data.length; i++) {
    this.data[i]=128 + Math.round(127 * this.data[i]);
  }
  return this;
};

Sound.prototype.finish = function() {
  // Assertions
  if (this.finished) {throw "This Sound was already finished";}
  this.finished = true;

  // Convert the data into valid WAV input
  this._convert255();

  // Create the WAV file
  var wave = new RIFFWAVE();
  wave.header.sampleRate = this.sampleRate;
  wave.header.numChannels = 1;
  wave.Make(this.data);

  // Create the HTML Audio Tag
  this.audio = new Audio();
  this.audio.src = wave.dataURI;

  this.audio.loop = false;
  this.audio.addEventListener('ended', function() {
    if (this.loop) {
      this.currentTime = 0;
      this.play();
    }
  }, false);

  return this;
};


/*
 * Audio Controls for the Sound once its finished
 */
Sound.prototype.play = function() {
  if (!this.finished) {this.finish();}
  this.audio.loop = false;
  this.audio.play();

  return this;
};
Sound.prototype.pause = function() {
  // Assertions
  if (!this.finished) {throw "The Sound is Unfinished";}
  this.audio.pause();

  return this;
};
Sound.prototype.loop = function() {
  if (!this.finished) {this.finish();}
  this.audio.loop = true;
  this.audio.play();

  return this;
};



var sampleRate = 44100;
var ringback = new Sound(sampleRate)
  .add().tone(440, 2).tone(480, 2);
  // .add().silence(4);

setTimeout(function() { ringback.play(); }, 10);

