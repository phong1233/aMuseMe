import React, { Component } from "react";
import "./App.css";
import Header from "./Header.js";
import Button from "@material-ui/core/Button";
import SkipNextIcon from "@material-ui/icons/SkipNext";
import SkipPreviousIcon from "@material-ui/icons/SkipPrevious";
import ButtonGroup from "@material-ui/core/ButtonGroup";
import Container from "@material-ui/core/Container";
import Box from "@material-ui/core/Box";
import PlayArrowIcon from "@material-ui/icons/PlayArrow";

class App extends Component {
  render() {
    return (
      <Container maxwidth="sm">
        <Header />
        <div className="center">
          <Box size="100%" width="100%"></Box>
        </div>
        <div className="buttonCenter">
          <ButtonGroup variant="text">
            <Button>
              <SkipPreviousIcon />
            </Button>
            <Button>
              <PlayArrowIcon />
            </Button>
            <Button>
              <SkipNextIcon />
            </Button>
          </ButtonGroup>
        </div>
      </Container>
    );
  }
}

export default App;
