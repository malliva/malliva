import { render } from '@testing-library/react';

import MarketAppLandingPage from './market-app-landing-page';

describe('MarketAppLandingPage', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppLandingPage />);
    expect(baseElement).toBeTruthy();
  });
});
