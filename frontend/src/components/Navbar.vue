<template>
  <nav>
    <v-toolbar fixed app color="#00AE3A" class="navbar">
      <v-app-bar-nav-icon
        app
        class="black--text"
        @click="drawer = !drawer"
      ></v-app-bar-nav-icon>
      <!-- <v-toolbar-title class=" black--text text-uppercase">
        <span>Acupulco </span>
        <span class="font-weight-light">Design</span>
      </v-toolbar-title> -->
      <v-spacer></v-spacer>
      <v-menu transition="slide-y-transition" bottom open-on-hover >
        <template v-slot:activator="{ on, attrs }">
          <v-btn  large v-bind="attrs" v-on="on" color="#ff9f1c" class="mx-2">Explore</v-btn>
        </template>
        <v-list>
          <v-list-item v-for="category in categories" :key="category.title">
            <v-list-item-title>{{ category.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
      <v-btn rounded dark large color="#011627">
        <span large>
          Login
        </span>
        <v-icon right>mdi-login-variant</v-icon>
      </v-btn>
    </v-toolbar>
    <v-navigation-drawer
      d-flex-column
      v-model="drawer"
      temporary
      app
      src="@/assets/images/cody-mclain-Dq5P6eWZXNY-unsplash.jpg"
      width="20%"
    >
      <v-list>
        <v-spacer></v-spacer>
        <v-list-item>
          <v-app-bar-nav-icon
            app
            class="white--text"
            @click="drawer = !drawer"
          ></v-app-bar-nav-icon>
        </v-list-item>
        <v-list-item>
          <v-list-item-avatar>
            <v-img
              src="@/assets/images/pineapple-supply-co-NgDapgpAiTE-unsplash.jpg"
            ></v-img>
          </v-list-item-avatar>
        </v-list-item>
        <v-list-item v-for="category in categories" :key="category.title">
          <v-list-item-content>
            <v-btn>
              <span>
                {{ category.title }}
              </span>
            </v-btn>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      categoris: [],
      drawer: false,
      links: [
        { text: "Dashboard", route: "/" },
        { text: "My Projects", route: "/projects" },
        { text: "Team", route: "/team" }
      ]
    };
  },
  created() {
    axios.get("http://127.0.0.1:8000/api/category/").then(response => {
      this.categories = response.data;
    });
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Engagement&display=swap");


.navbar {
  font-size: 4px;
}
</style>