# Nova Sonic Simple Implementation - Code Analysis

This document provides a detailed analysis of the `nova_sonic_simple.py` implementation, which demonstrates the basic integration with Amazon Nova Sonic model for speech-to-speech conversations.

## Overview

The code implements a simple speech-to-speech conversation system using Amazon's Nova Sonic model through AWS Bedrock. It captures audio from the microphone, sends it to the Nova Sonic model, and plays back the model's audio responses. This implementation demonstrates the event structure used in the bidirectional streaming API but does not support barge-in functionality.

## Key Components

### 1. Audio Configuration

```python
# Audio configuration
INPUT_SAMPLE_RATE = 16000  # Sample rate for microphone input
OUTPUT_SAMPLE_RATE = 24000  # Sample rate for audio output
CHANNELS = 1  # Mono audio
FORMAT = pyaudio.paInt16  # 16-bit audio format
CHUNK_SIZE = 1024  # Size of audio chunks processed at once
```

These parameters define the audio settings for both input (microphone) and output (speakers). The Nova Sonic model expects 16kHz input audio and produces 24kHz output audio.

### 2. SimpleNovaSonic Class

The main class that handles the interaction with the Nova Sonic model.

#### Initialization

```python
def __init__(self, model_id='amazon.nova-sonic-v1:0', region='us-east-1'):
    self.model_id = model_id  # Nova Sonic model ID
    self.region = region  # AWS region
    self.client = None  # Bedrock client
    self.stream = None  # Bidirectional stream
    self.response = None  # Task for processing responses
    self.is_active = False  # Flag to control the session state
    self.prompt_name = str(uuid.uuid4())  # Unique ID for the prompt
    self.content_name = str(uuid.uuid4())  # Unique ID for the content
    self.audio_content_name = str(uuid.uuid4())  # Unique ID for audio content
    self.audio_queue = asyncio.Queue()  # Queue for audio playback
    self.role = None  # Current role (USER or ASSISTANT)
    self.display_assistant_text = False  # Flag to control text display
```

The constructor initializes various attributes needed for the session, including unique identifiers for the prompt and content, which are required by the Nova Sonic API.

#### Client Initialization

```python
def _initialize_client(self):
    """Initialize the Bedrock client."""
    config = Config(
        endpoint_uri=f"https://bedrock-runtime.{self.region}.amazonaws.com",
        region=self.region,
        aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
        http_auth_scheme_resolver=HTTPAuthSchemeResolver(),
        http_auth_schemes={"aws.auth#sigv4": SigV4AuthScheme()}
    )
    self.client = BedrockRuntimeClient(config=config)
```

This method sets up the AWS Bedrock client with the appropriate configuration, including authentication using environment variables.

### 3. Session Management

#### Starting a Session

```python
async def start_session(self):
    """Start a new session with Nova Sonic."""
    # Initialize client if not already done
    if not self.client:
        self._initialize_client()
        
    # Initialize the bidirectional stream
    self.stream = await self.client.invoke_model_with_bidirectional_stream(
        InvokeModelWithBidirectionalStreamOperationInput(model_id=self.model_id)
    )
    self.is_active = True
    
    # Send session start event - configures inference parameters
    # Send prompt start event - configures output formats
    # Send system prompt - sets the assistant's behavior
    # Start processing responses
```

This method establishes the connection with the Nova Sonic model and sets up the session by sending several initialization events:

1. **Session Start Event**: Configures inference parameters like temperature and top-p.
2. **Prompt Start Event**: Configures text and audio output formats.
3. **System Prompt**: Defines the assistant's behavior and personality.

#### Ending a Session

```python
async def end_session(self):
    """End the session."""
    if not self.is_active:
        return
        
    # Send prompt end event
    # Send session end event
    # Close the stream
```

This method properly terminates the session by sending the appropriate end events and closing the stream.

### 4. Audio Handling

#### Audio Input

```python
async def start_audio_input(self):
    """Start audio input stream."""
    # Send audio content start event - configures audio input format
```

```python
async def send_audio_chunk(self, audio_bytes):
    """Send an audio chunk to the stream."""
    # Base64 encode the audio chunk
    # Send audio input event with the encoded chunk
```

```python
async def end_audio_input(self):
    """End audio input stream."""
    # Send audio content end event
```

These methods handle the audio input lifecycle:
1. Start the audio input by configuring the format (16kHz, 16-bit, mono).
2. Send audio chunks as they are captured from the microphone.
3. End the audio input when the session is terminated.

#### Audio Output

```python
async def _process_responses(self):
    """Process responses from the stream."""
    # Continuously receive and process events from the stream
    # Handle content start events - determine the role (USER or ASSISTANT)
    # Handle text output events - display transcripts
    # Handle audio output events - queue audio for playback
```

```python
async def play_audio(self):
    """Play audio responses."""
    # Initialize PyAudio output stream
    # Continuously get audio chunks from the queue and play them
```

These methods handle the audio output lifecycle:
1. Process responses from the Nova Sonic model, extracting text and audio.
2. Queue audio chunks for playback.
3. Play audio chunks through the speakers.

### 5. Main Execution Flow

```python
async def main():
    # Create Nova Sonic client
    nova_client = SimpleNovaSonic()
    
    # Start session
    await nova_client.start_session()
    
    # Start audio playback task
    playback_task = asyncio.create_task(nova_client.play_audio())
    
    # Start audio capture task
    capture_task = asyncio.create_task(nova_client.capture_audio())
    
    # Wait for user to press Enter to stop
    await asyncio.get_event_loop().run_in_executor(None, input)
    
    # End session and clean up tasks
```

The main function orchestrates the entire process:
1. Create the Nova Sonic client.
2. Start the session with the model.
3. Start concurrent tasks for audio playback and capture.
4. Wait for the user to press Enter to stop.
5. Clean up by ending the session and canceling tasks.

## Event Structure

The Nova Sonic API uses a structured event-based protocol for bidirectional communication. Key events include:

1. **Session Events**:
   - `sessionStart`: Initializes the session with inference parameters.
   - `sessionEnd`: Terminates the session.

2. **Prompt Events**:
   - `promptStart`: Begins a new prompt with output configuration.
   - `promptEnd`: Ends the current prompt.

3. **Content Events**:
   - `contentStart`: Begins a content segment (text or audio) with role and configuration.
   - `contentEnd`: Ends a content segment.
   - `textInput`: Sends text input to the model.
   - `audioInput`: Sends audio input to the model.
   - `textOutput`: Receives text output from the model.
   - `audioOutput`: Receives audio output from the model.

## Limitations of this Implementation

1. **No Barge-in Support**: This implementation does not allow interrupting the assistant while it's speaking.
2. **Simple One-way Communication**: The communication flow is more sequential rather than truly bidirectional.
3. **Basic Error Handling**: Error handling is minimal and could be improved for production use.
4. **Fixed System Prompt**: The system prompt is hardcoded and not easily configurable.

## Conclusion

This implementation provides a basic foundation for understanding how to interact with the Nova Sonic model through the bidirectional streaming API. It demonstrates the event structure and flow but lacks some advanced features like barge-in that are available in the more sophisticated implementations (`nova_sonic.py` and `nova_sonic_tool_use.py`).
