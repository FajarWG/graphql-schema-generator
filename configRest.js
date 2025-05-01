const path = require("path");

module.exports = [
  {
    type: "file",
    path: path.join(__dirname, "/dumpJson/input.json"),
    typeName: "LoginResponse",
  },
  {
    type: "file",
    path: path.join(__dirname, "/dumpJson/projects.json"),
    typeName: "Projects",
  },
  {
    type: "file",
    path: path.join(__dirname, "/dumpJson/prompt.json"),
    typeName: "Prompt",
  },
  {
    type: "file",
    path: path.join(__dirname, "/dumpJson/topic.json"),
    typeName: "Topic",
  },
  {
    type: "file",
    path: path.join(__dirname, "/dumpJson/sna.json"),
    typeName: "SNA",
  },
  // {
  //   type: "api",
  //   url: "https://socialabs-gateway.azure-api.net/topic/topic-by-project/674f063d7ae271700e0f711a",
  //   typeName: "TopicByProject",
  // },
  // {
  //   type: "api",
  //   url: "https://socialabs-gateway.azure-api.net/chatbot/prompt?project_id=674f063d7ae271700e0f711a",
  //   typeName: "PromptProject",
  // },
];
