<template>
  <v-footer color="#00AE3A">
    <v-row justify="center" no-gutters>
      <v-btn
        v-for="link in links"
        :key="link"
        color="#fec601"
        rounded
        class="my-2 mx-1 black--text"
      >
        {{ link }}
      </v-btn>
      <v-col class="py-4 text-center" cols="12">
        {{ new Date().getFullYear() }} — <strong>Acupulco Design</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>


<script>
export default {
  data: () => ({
    links: ["Home", "About Us", "Team", "Services", "Blog", "Contact Us"]
  })
};
</script>

