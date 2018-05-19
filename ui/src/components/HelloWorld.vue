<template>
  <div class="hello">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data () {
    return {
      message: 'Loading...'
    }
  },
  methods: {
    getMessage () {
      axios.get('/api/message')
        .then(response => {
          this.message = response.data.message
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getMessage()
  }
}
</script>
