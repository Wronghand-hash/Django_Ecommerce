<template>
 <v-container>
  <v-card>
    <v-card-title>
      please sign in to continue
    </v-card-title>
    <v-card-text>
      
      <form v-on:submit.prevent="login">
        <div>
          <input
            type="text"
            name="username"
            id="user"
            v-model="username"
            placeholder="Username"
          />
        </div>
        <div>
          <input
            type="password"
            name="password"
            id="pass"
            v-model="password"
            placeholder="Password"
          />
        </div>
        <v-card-action>
        <v-btn @click="login">Login</v-btn>
        <p v-if="incorrectAuth">incorrect credentials</p>
        </v-card-action>
      </form>
    </v-card-text>
  </v-card>
  </v-container>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
      incorrectAuth: false
    };
  },
  methods: {
    login() {
      this.$store
        .dispatch("userLogin", {
          username: this.username,
          password: this.password
        })
        .then(() => {
          this.$router.push({ name: "Home" });
        })
        .catch(err => {
          console.log(err);
          this.incorrectAuth = true;
        });
    }
  }
};
</script>