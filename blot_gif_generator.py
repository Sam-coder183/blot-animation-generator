from PIL import Image
image_src_input = input("Enter image file paths (separated by comma): ")
image_paths = image_src_input.split(",")

output_images = []
for image_path in image_paths:
    try:
        pass
    
    except Exception as e:
        print("Error:", str(e))
        image = Image.open(image_path.strip())
        width, height = image.size

        image = image.resize((width, int(height * width / width)))
        pixels = image.load()

        output_array = []
        for y in range(height):
            output_array.append([])
            for x in range(width):
                r, g, b = pixels[x, y]
                avg = (r + g + b) // 3
                output_array[y].append(avg)

        output_images.append(output_array)

    except Exception as e:
        print("Error processing image:", str(e))

output_string = "images = ["
for image_array in output_images:
    output_string += "["
    for row in image_array:
        output_string += "[" + ", ".join(str(pixel) for pixel in row) + "],"
    output_string = output_string[:-1] + "],"
output_string = output_string[:-1] + "]"

print(output_string)


width, height = image.size

def image_to_array(image_src_input, width): 
    try:
        image = image.resize((width, int(height * width / width)))
        pixels = image.load()

        output_array = []
        for y in range(height):
            output_array.append([])
            for x in range(width):
                r, g, b = pixels[x, y]
                avg = (r + g + b) // 3
                output_array[y].append(avg)

        output_string = "image = ["
        for row in output_array:
            output_string += "["
            output_string += ", ".join(str(pixel) for pixel in row)
            output_string += "],"
        output_string = output_string[:-1] + "]"

        print(output_string)
    except Exception as e:
        print("Error:", str(e))

plot_script = """
/*
@title: SineArt
@author: Ruben Stenlund
@snapshot: lion.png
*/

// image array - generated using the imagegenerator.html file

const scale = 1;
// amount of horizontal steps (lower number will give higher resolution)
const step_x = 0.1
const step_y = 3
// multiplier for the wave frequency
const freq_multiplier = 1
// multiplier for the wave amplitude
const amplitude_multiplier = 1.5

function lerp(a, b, alpha) {
  return a + alpha * (b- a)
}

function drawImage(image) {
  const t = new bt.Turtle();

  const width = image[0].length * scale;
  const height = image.length * scale;

  setDocDimensions(width, height);
  let sinusFactor = 1
  const finalLines = [];
  for (let y = 0; y < image.length - 1; y+=Math.round(step_y)) {
    sinusFactor = 1
    let pos_y = image.length - y * scale;
    t.up()
    t.goTo([0, pos_y])
    t.down()

    for (let x = 0; x < image[0].length - 1; x+=step_x) {
      let x_index = Math.round(x)
      let pos_x = x * scale;
      let pixel = 255-image[y][x_index]
      sinusFactor = lerp(sinusFactor, x * pixel / 255, 0.06)
      let sinus_change = Math.sin(sinusFactor*freq_multiplier) * pixel / 300
      t.goTo([pos_x, pos_y + sinus_change * amplitude_multiplier]);
    }
  }


  bt.join(finalLines, t.lines());

  // center piece
  const cc = bt.bounds(finalLines).cc;
  bt.translate(finalLines, [width / 2, height / 2], cc);

  
}
 
    function animate_lines(){


    }


   function drawLines(lines) {
    drawLines(finalLines);
    }



function fetchCells() {
  drawImage(image);
}


fetchCells();
"""