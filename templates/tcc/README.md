#Demo

http://andromeda.nitc.ac.in/~saurabh/popbox/

# jQuery PopBox

jQuery PopBox is a simple balloon UI element.

# Usage
jQuery PopBox requires a specific HTML structure in order to work. There is also a small stylesheet that can be used. jQuery is a dependency.

The HTML structure looks like this.
```html
<div class='popbox'>
  <a class='open' href='#'>Click Here!</a>

  <div class='collapse'>
    <div class='box'>
      <div class='arrow'></div>
      <div class='arrow-border'></div>

      Content in PopBox goes here :)

      <a href="#" class="close">close</a>
    </div>
  </div>
</div>
```

Invoke the plugin by calling it on a selector like normal.
```html
<script type='text/javascript'>
   $(document).ready(function(){
     $('.popbox').popbox();
   });
</script>
```

If there are any CSS class name conflicts, they can be overridden.

```html
<script type='text/javascript'>
   $(document).ready(function(){
     $('.popbox').popbox({
       'open'          : '.open',
       'box'           : '.box',
       'arrow'         : '.arrow',
       'arrow_border'  : '.arrow_border',
       'close'         : '.close'
      });
   });
</script>
```


## Credits

jQuery PopBox developed by saurabh sinha https://www.facebook.com/saurabh.nitc


## License

MIT license:

http://www.opensource.org/licenses/MIT
