<template>
  <div class="hello">
    <h1>Fibonacci</h1>
    <div>
      The {{ number }} {{ suf }} numebr of Fibonacci is {{ fibonacci }}!
    </div>
  </div>
</template>

<script>

  import axios from "axios";

  export default {
    name: 'Fibonacci',
    props: {
      msg: String
    },
    data() {
      return {
        number: 1,
        fibonacci: 1,
        suf: 'st'
      };
    },
    async mounted() {
      await axios({ method: "GET", "url": "http://progetto.las.unive/number" })
          .then(result => {
            this.number = result.data['number'];
            this.suf = this.number == 1 ? 'st' : (this.number == 2 ? 'nd' : 'th');
          }, error => {
            console.error(error);
          });

      await axios({ method: "GET", "url": `http://progetto.las.unive/fibonacci?number=${this.number}` })
          .then(result => {
            this.fibonacci = result.data['fibonacci'];
          }, error => {
            console.error(error);
          });
    }
  }
</script>
