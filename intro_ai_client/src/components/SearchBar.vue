<template>
    <v-card
      class="mx-auto"
      color="surface-light"
      max-width="80%"
      height="70%"
      style="top: 12%; border-radius:16px;"
    >
      <v-card-text>
        <v-text-field
            style="margin: auto;width: 80%;top: 50%;"
          :loading="loading"
          append-inner-icon="mdi-magnify"
          density="compact"
          label="Search templates"
          variant="solo"
          hide-details
          single-line
          @click:append-inner="onClick"
        ></v-text-field>
      </v-card-text>
      <v-list
        :items="items"
        item-title="name"
        item-value="id"
        ></v-list>
    </v-card>


</template>

<script>
export default {
    data: () => ({
        loaded: false,
        loading: false,
        items: [
            {
            name: 'Item #1',
            id: 1,
            },
            {
            name: 'Item #2',
            id: 2,
            },
            {
            name: 'Item #3',
            id: 3,
            },
        ],
    }),

    methods: {
    onClick () {
        this.loading = true
        
        setTimeout(() => {
            this.loading = false
            this.loaded = true
        }, 1000)
    },
    },
}
</script>

<style>
  .v-text-field input {
    font-size: 2em;
  }
</style>