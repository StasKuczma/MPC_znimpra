import mujoco
import mujoco_viewer


class Pendulum():
    def __init__(self) -> None:
        self.dt = 0.001
        self.b = 0.05
        self.l = 0.3
        self.m = 1.
        self.model, self.data = self.create_mujoco_model()
        self.viewer = mujoco_viewer.MujocoViewer(self.model, self.data)

    def create_mujoco_model(self):
        pendulum = f"""
        <mujoco>
        <option timestep="{self.dt}" integrator="RK4">
            <flag energy="enable"/>
        </option>

        <default>
            <joint type="hinge" axis="0 -1 0"/>
            <geom type="capsule" size=".02"/>
        </default>

        <worldbody>
            <light pos="0 -.4 1"/>
            <camera name="fixed" pos="0 -2 0.2" xyaxes="1 0 0 0 0 1"/>

            <PUT YOUR OBJECT HERE>

            </body>
        </worldbody>

        <actuator>
            <motor name="my_motor" joint="joint0" gear="1"/>
        </actuator>
        </mujoco>
        """
        
        model = mujoco.MjModel.from_xml_string(pendulum)
        data = mujoco.MjData(model)
        return model, data

    def init_episode(self):
        mujoco.mj_resetData(self.model, self.data)

    def step_sim(self, u, render=False):
        self.data.ctrl[0] = u
        mujoco.mj_step(self.model, self.data)
        if render and self.viewer.is_alive:
            self.viewer.render()

    def set_state(self, q, q_dot):
        raise NotImplementedError

    def get_state(self):
        raise NotImplementedError